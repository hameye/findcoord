###############################################################################
#    This file is part of FindCoord developed at the University of Lorraine
#    by the GeoRessources Laboratory. FindCoord helps recalculating
#    coordinates of a series of points in a new system from reference
#    points measured in the initial an final coordinate systems
#
#    FindCoord is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    FindCoord is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with FindCoord.  If not, see <https://www.gnu.org/licenses/>
#
#    Author = Hadrien Meyer
#    Contact = jean.cauzid@univ-lorraine.fr
#    Copyright (C) 2019, 2020 H. Meyer, University of Lorraine
#
###############################################################################
__author__ = "Hadrien Meyer"
__organization__ = "ENSG - UMR GeoRessources N°7359 - Université de Lorraine"
__email__ = "meyerhadrien96@gmail.com"
__date__ = "March, 2020"

import os
import pandas as pd
from skimage import transform as tf


class transformation:
    """ Class that allows to compute the transformation of
    coordinates given    some landmarks between two systems.

    Based on scikit-image and made for multi-platform
    spectroscopy analsyses : it is a simple overlay
    that open a spreadsheet with known coordinates
    and write in a second spreadsheet the c∏alculated coordinates.

    Main functions are transform() and
    extract_mesures_final().
    Other functions are just
    accessors in order to validate the tranfsormation.

    Accepted type of spreadsheet : .txt, .csv, .xlsx

    Parameters
    ----------
    input_filename : x,y(,z) spreadsheet
        Known coordinates.
    output_filename : x,y(,z) spreadsheet
        Coordinates to be calculated.

    References
    ----------
    Scikit-Image :
    https://scikit-image.org/docs/stable/api/skimage.transform.html#skimage.transform.AffineTransform
    """

    def __init__(self, input_filename: str, output_filename: str):
        """ Load the input and
        output files and extract values to put into arrays
        """

        self.input_ = input_filename
        self.output_ = output_filename

        # Create Dataframes from the textfiles
        if self.input_.split('.')[-1] in ('csv', 'txt'):
            self.input_data = pd.read_csv(input_filename)
            self.output_data = pd.read_csv(output_filename)
        else:
            self.input_data = pd.read_excel(input_filename, header=1)
            self.output_data = pd.read_excel(output_filename, header=1)

    def calculate_coordinates(self, type='Proj'):
        """ In laboratory spectroscopy the transformation
        should only be affine (Rotation,Translation and Shear).
        But in general cases, the transformation could
        also have deformation and the transformation is
        a projection.
        See Mathematical definition of affine
        transformation and Projection (Homography) for more details. """
        self.repere_init_array_ = self.input_data.loc[
            self.input_data['Type'].str.contains('ef')].to_numpy()[:, 1:]
        self.repere_final_array_ = self.output_data.loc[
            self.output_data['Type'].str.contains('ef')].to_numpy()[:, 1:]
        self.mesures_init_array_ = self.input_data.loc[
            self.input_data['Type'].str.contains('easure')].to_numpy()[:, 1:]

        if type == 'Affine':
            self.transformation_ = tf.AffineTransform()
            self.transformation_.estimate(
                self.repere_init_array_, self.repere_final_array_)
            self.mesures_final_array_ = self.transformation_(
                self.mesures_init_array_)

        if type == 'Proj':
            self.transformation_ = tf.ProjectiveTransform()
            self.transformation_.estimate(
                self.repere_init_array_, self.repere_final_array_)
            self.mesures_final_array_ = self.transformation_(
                self.mesures_init_array_)

    def get_transform_matrix(self):
        """ Return the array of the transformation matrix. """
        return self.transformation_.params

    def get_transform_repere(self):
        """ Return the transformation of the Landmarks
        done by the matrix. Usefull to compare the the
        true and the calculated landmarks """
        return self.transformation_(self.repere_init_array_)

    def extract_coordinates(self):
        """ Write the calculated coordinates into the output textfile. """
        prefix = os.path.commonprefix(
            [self.input_data.iloc[-1]['Type'],
             self.input_data.iloc[-2]['Type']])
        fd = open(self.output_, "a")
        fd.write('\n')
        for i in range(self.mesures_final_array_.shape[0]):
            fd.write(
                '{},{},{}\n'.format(
                    prefix + str(
                        i + 1),
                    round(
                        self.mesures_final_array_[
                            i,
                            0],
                        2),
                    round(
                        self.mesures_final_array_[
                            i,
                            1],
                        2)))
        fd.close()
