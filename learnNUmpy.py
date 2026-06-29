import numpy as np

# Numpy arrays
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([1, 2, 3])
five = array_1d + 10
sum_1d = np.sum(array_1d)
print("Sum of 1D array:", five, array_1d)
print("The type of array_1d is:", type(array_1d))
print("The shape of array_1d is:", array_1d.dtype)
float_array = np.array([1.0, 2.0, 3.0])
print("The type of elements found in this aarray:", float_array.dtype)
print("The type of float_arry is:", type(float_array))

zeros_array = np.zeros((3, 4))
print("The shape of zeros_array is:", zeros_array.shape)
print("The size of zeros_array is:", zeros_array.size)
print("The number of dimensions of zeros_array is:", zeros_array.ndim)
print("The dtypes of zeros_array is:", zeros_array.dtype)
print("THe array itself is:", zeros_array)

normal_distribution_array = np.random.normal(0, 1, (3, 4))
