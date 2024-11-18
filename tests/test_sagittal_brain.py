import sys
import os
import numpy as np
import tempfile

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sagittal_average.sagittal_brain import run_averages


def test_run_averages():
    with tempfile.TemporaryDirectory() as temp_dir:
        input_file = os.path.join(temp_dir, "brain_sample.csv")
        output_file = os.path.join(temp_dir, "brain_average.csv")

        data_input = np.zeros((20, 20))
        data_input[-1, :] = 1
        np.savetxt(input_file, data_input, fmt='%d', delimiter=',')

        expected = np.zeros(20)
        expected[-1] = 1

        run_averages(file_input=input_file, file_output=output_file)

        result = np.loadtxt(output_file, delimiter=',')
        np.testing.assert_array_equal(result, expected)
