import numpy as np
from sagittal_average.sagittal_brain import run_averages

def test_run_averages(tmp_path):
    """
    Test the run_averages function to ensure it calculates row averages correctly.
    """
    # Step 1: Create an input dataset
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1

    # Save it to a temporary file
    input_file = tmp_path / "brain_sample.csv"
    np.savetxt(input_file, data_input, fmt='%d', delimiter=',')

    # Step 2: Create the expected result
    expected = np.zeros(20)
    expected[-1] = 1

    # Step 3: Call the function with the temporary files
    output_file = tmp_path / "brain_average.csv"
    run_averages(file_input=input_file, file_output=output_file)

    # Step 4: Load the result
    result = np.loadtxt(output_file, delimiter=',')

    # Step 5: Compare the result with the expected values
    np.testing.assert_array_equal(result, expected)
