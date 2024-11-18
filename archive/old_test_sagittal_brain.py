import numpy as np
import subprocess

ls = [[j+1 for i in range(20)] for j in range(20)]
input = np.array(ls, dtype=int)
expected = np.array([float(i+1) for i in range(20)])

np.savetxt('brain_sample.csv', input, fmt='%i', delimiter=',')

subprocess.run(["python", "sagittal_brain.py"])
output = np.loadtxt('brain_average.csv', dtype=float,  delimiter=',')

np.testing.assert_array_equal(expected, output)
