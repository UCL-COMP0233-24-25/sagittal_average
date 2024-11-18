
import pytest
import numpy as np
import subprocess
from sagittal_brain.sagittal_brain import run_averages

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')
#changed the axis from 0 to 1, the previous code was looing at the wrong plane, hence the non-zero averages


subprocess.run(["python", "src/sagittal_brain/sagittal_brain.py"], shell=True)
data_output = np.zeros((20,1))
data_output[-1, :] = 1.0
np.savetxt("brain_average_output.csv", data_output, fmt='%d', delimiter=',')

def test_function(file_path_expected = "brain_average_output.csv", file_path_actual = "brain_average.csv"):        
    expected_result = np.loadtxt(file_path_expected, delimiter=',')
    run_averages("brain_sample.csv", "brain_average.csv")
    actual_result = np.loadtxt(file_path_actual, delimiter=',')
    assert np.all(actual_result) == np.all(expected_result), "The results dont match the expected"