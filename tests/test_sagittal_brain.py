import numpy as np
from sagittal_average import sagittal_brain
from sagittal_average import data_collect
import csv

def test_code():
    input = [[1,1,1], [0, 0, 0], [0, 0, 0]]
    result = np.mean(input, axis=1) #求每一行的均值
    expect = np.array([1, 0, 0])
    assert np.all(result==expect)
    
def test_func(): #26
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1
    file = data_collect.save_array2CSV(data_input)
    with open('brain_sample.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_input)
    
    sagittal_brain.run_averages(file_input="brain_sample.csv", file_output='brain_average.csv')
    
    output = data_collect.readCSV(filepath = 'brain_average.csv') # output = np.loadtxt('brain_average.csv', delimiter=',')
    
    expect = np.array([0.]*20)
    expect[-1] = 1.
    
    np.testing.assert_array_equal(output, expect)