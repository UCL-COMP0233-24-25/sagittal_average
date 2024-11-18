import numpy as np

TEST_DIR = '/Users/sirbucks/Desktop/UCL/Coding/COMP0233_Research_SWE_Python/session_7/part2/sagittal_average/'

import numpy as np
from pathlib import Path
import tempfile
from src.sagittal_average.sagittal_brain import run_averages

def test_sagittal_average():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create an input dataset
        data_input = np.zeros((20, 20))
        data_input[-1, :] = 1

        # Save it into a file in the temporary directory
        input_file = Path(temp_dir) / "brain_sample.csv"
        np.savetxt(input_file, data_input, fmt='%d', delimiter=',')

        # Create an array with expected result
        expected = np.zeros(20)
        expected[-1] = 1

        # Call the function with the files in the temporary directory
        output_file = Path(temp_dir) / "brain_average.csv"
        run_averages(file_input=str(input_file), 
                     file_output=str(output_file))

        # Load the result
        result = np.loadtxt(output_file, delimiter=',')

        # Compare the result with the expected values
        np.testing.assert_array_equal(result, expected)