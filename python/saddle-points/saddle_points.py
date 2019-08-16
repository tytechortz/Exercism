import numpy as np

def saddle_points(matrix):

    matrix = np.asarray(matrix)
    print(matrix)
    print(matrix.shape)
    for element in matrix.flat:
        print(element)
saddle_points([[3, 1, 3], [3, 2, 4]])