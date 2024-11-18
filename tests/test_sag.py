import numpy as np

def run_averages(file_input='tests/test_brain_sample.csv', file_output='tests/test_brain_average.csv'):
    """
    Calculates the average through the coronal planes
    The input file should has as many columns as coronal planes
    The rows are intersections of the sagittal/horizontal planes

    The result is the average for each sagittal/horizontal plane (rows)
    """
    # Open the file to analyse
    planes = np.loadtxt(file_input, dtype=int,  delimiter=',')

    # Calculates the averages through the sagittal/horizontal planes
    # and makes it as a row vector
    averages = planes.mean(axis=1)[np.newaxis, :]

    # write it out on my file
    np.savetxt(file_output, averages, fmt='%.1f', delimiter=',')

def test_brain_sample():
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1

    np.savetxt("tests/test_brain_sample.csv", data_input, fmt='%d', delimiter=',')
 
    # The expeted result is all zeros, except the last one, it should be 1
    expected = np.zeros(20)
    expected[-1] = 1



    run_averages(file_input = "tests/test_brain_sample.csv",
                 file_output="tests/test_brain_average.csv")
    
    result = np.loadtxt("tests/test_brain_average.csv",  delimiter=',')

    np.testing.assert_array_equal(result, expected)

#PYTHONPATH=$PYTHONPATH:"."
#python sagittal_average_jg/tests/test.py