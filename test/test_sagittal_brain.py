import unittest
import numpy as np
from pathlib import Path
from src.sagittal_avg.sagittal_brain import run_averages  # Adjust import path as needed

class TestRunAverages(unittest.TestCase):
    def setUp(self):
        # Create temporary directory for test files
        self.test_dir = Path(__file__).parent
        self.input_file = self.test_dir / "brain_sample.csv"
        self.output_file = self.test_dir / "brain_average.csv"
        
        # Create input dataset
        data_input = np.zeros((20, 20))
        data_input[-1, :] = 1
        np.savetxt(self.input_file, data_input, fmt='%d', delimiter=',')

        # Expected result
        self.expected = np.zeros(20)
        self.expected[-1] = 1

    def tearDown(self):
        # Clean up test files
        if self.input_file.exists():
            self.input_file.unlink()
        if self.output_file.exists():
            self.output_file.unlink()

    def test_run_averages(self):
        # Call the function with the input file and save the output
        run_averages(file_input=str(self.input_file), file_output=str(self.output_file))
        
        # Load the result from the output file
        result = np.loadtxt(self.output_file, delimiter=',')
        
        # Compare the result with the expected values
        np.testing.assert_array_equal(result, self.expected)

if __name__ == '__main__':
    unittest.main()
