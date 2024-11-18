import numpy as np
from src.brain_average.sagittal_brain import run_averages
import subprocess

test_input = np.zeros((20, 20))
test_input[-1, :] = 1.

expected = np.zeros(20)
expected[-1] = 1.

# Save input to brain_sample.csv
np.savetxt("brain_sample.csv", test_input, fmt='%d', delimiter=',')


# run sagital_brain.py
subprocess.run(["python", "sagittal_brain.py", "brain_sample.csv", "brain_average.csv"])


# Read output from brain_average.csv
output = np.loadtxt("brain_average.csv", delimiter=',')

# Compare the outpare with the expected output
assert np.all(output) == np.all(expected)

