def test_run_averages():
    from sagittal_average import sagittal_brain
    import numpy as np

    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1
    np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

    expected = np.zeros(20)
    expected[-1] = 1

    sagittal_brain.run_averages(file_input="brain_sample.csv", file_output="brain_average.csv")
    result = np.loadtxt("brain_average.csv", delimiter=',')
    np.testing.assert_array_equal(result, expected)

