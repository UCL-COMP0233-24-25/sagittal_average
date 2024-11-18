import os
import numpy as np
import pytest
from unittest.mock import patch
from io import StringIO
import sys
# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sagittal_brain import run_averages  # Now import the function



@pytest.fixture
def mock_input_file():
    # Create a temporary CSV file with mock data
    mock_data = "1,2,3\n4,5,6\n7,8,9\n"
    file_path = "brain_sample.csv"
    with open(file_path, 'w') as f:
        f.write(mock_data)
    yield file_path
    os.remove(file_path)


@pytest.fixture
def mock_output_file():
    # Create a temporary output file path for the result
    return "brain_average.csv"


def test_run_averages(mock_input_file, mock_output_file):
    # Call the function with mock files
    run_averages(mock_input_file, mock_output_file)

    # Check if the output file exists
    assert os.path.exists(mock_output_file)

    # Read the content of the output file and check if averages are correct
    expected_output = "4.0,5.0,6.0\n"  # The expected averages of the mock input data
    with open(mock_output_file, 'r') as f:
        output_data = f.read()

    assert output_data == expected_output

    # Clean up by removing the output file
    os.remove(mock_output_file)
