from pathlib import Path

import numpy as np
from sagittal_average.sagittal_brain import run_averages

TEST_DIR = Path(__file__).parent


def test_average():
    # Creates input file
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1
    # The expeted result is all zeros, except the last one, it should be 1
    expected = np.zeros(20)
    expected[-1] = 1

    np.savetxt(TEST_DIR / "brain_sample.csv", data_input, fmt="%d", delimiter=",")

    # run python program
    run_averages(
        file_input=TEST_DIR / "brain_sample.csv",
        file_output=TEST_DIR / "brain_average.csv",
    )

    # Check result
    result = np.loadtxt(TEST_DIR / "brain_average.csv", delimiter=",")
    np.testing.assert_array_equal(result, expected)
