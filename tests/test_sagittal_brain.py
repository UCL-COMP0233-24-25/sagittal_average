import numpy as np
import subprocess

from brain_average import run_averages

def test_average_brain():
    test_input = np.zeros((20, 20))
    test_input[-1, :] = 1.

    expected = np.zeros(20)
    expected[-1] = 1.

    # Save input to brain_sample.csv
    np.savetxt("brain_sample.csv", test_input, fmt='%d', delimiter=',')


    # run sagital_brain.py
    run_averages(file_input="brain_sample.csv",
                 file_output="brain_average.csv")



    # Read output from brain_average.csv
    output = np.loadtxt("brain_average.csv", delimiter=',')

    # Compare the outpare with the expected output
    assert np.all(output) == np.all(expected)

