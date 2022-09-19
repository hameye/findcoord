from re import I
import findcoord as fn
import pandas as pd

from pathlib import Path

THIS_DIR = Path(__file__)


def test_same():
    input_filename = f'{THIS_DIR.parent}/data/Input.txt'
    output_filename = f'{THIS_DIR.parent}/data/Output_same_mes.txt'
    blank = pd.read_csv(output_filename)
    TF = fn.transformation(input_filename, output_filename)
    TF.calculate_coordinates()
    TF.extract_coordinates()

    ref = pd.read_csv(f'{THIS_DIR.parent}/data/Input.txt')
    mes = pd.read_csv(output_filename)

    
    blank.to_csv(output_filename, index=False)
    pd.testing.assert_series_equal(ref['X'], mes['X'], check_dtype=False)
    pd.testing.assert_series_equal(ref['Y'], mes['Y'], check_dtype=False)


def test_random():
    input_filename = f'{THIS_DIR.parent}/data/Input.txt'
    output_filename = f'{THIS_DIR.parent}/data/Output_random_mes.txt'
    blank = pd.read_csv(output_filename)
    TF = fn.transformation(input_filename, output_filename)
    TF.calculate_coordinates()
    TF.extract_coordinates()

    ref = pd.read_csv(f'{THIS_DIR.parent}/data/Output_random_ref.txt')
    mes = pd.read_csv(output_filename)

    
    blank.to_csv(output_filename, index=False)
    pd.testing.assert_frame_equal(ref, mes)
