import numpy as np
import pytest
import subprocess
from src.sagittal_brain.sagittal_brain import run_averages

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("../src/sagittal_brain/brain_sample.csv", data_input, fmt='%d', delimiter=',')
#changed the axis from 0 to 1, the previous code was looing at the wrong plane, hence the non-zero averages


subprocess.run(["python", "../src/sagittal_brain/sagittal_brain.py"], shell=True)
data_output = np.zeros((20,1))
data_output[-1, :] = 1.0
np.savetxt("brain_average_output.csv", data_output, fmt='%d', delimiter=',')
expected_result = np.loadtxt("brain_average_output.csv", delimiter=',')
run_averages("../src/sagittal_brain/brain_sample.csv", "../src/sagittal_brain/brain_average.csv")
actual_result = np.loadtxt("../src/sagittal_brain/brain_average.csv", delimiter=',')
assert  np.all(actual_result) == np.all(expected_result), "Files are not equal"