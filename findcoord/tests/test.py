from findcoord.transform import findcoord
import numpy as np


def test_transformation():
    TF = findcoord('Input.txt', 'Output.txt')
    TF.calculate_coordinates()
    assert TF.mesures_final_array_.astype('float').all() == np.array(
        [
            [
                124.39044127361605, 36.80539040824413], [
                90.94469779584279, 39.44780410429261], [
                    114.56211846783388, 44.50945864359023], [
                        71.93591521394606, 40.41996830427888], [
                            173.90661742788063, 34.465107806445175]]).all()
