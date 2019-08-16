import numpy as np

def saddle_points(matrix):
    saddle_points = []
    matrix = np.asarray(matrix)
    print(len(matrix))
    print(matrix.shape)
    # print(matrix[1,1])
    print(matrix[0])
    print(matrix[:,0])

    for x in range(len(matrix)):
        for y in range(matrix.shape[1]):
            if matrix[x][y] >= max(matrix[x]) and matrix[x][y] == min(matrix[:,y]):
                saddle_points.append([x,y])
    print(saddle_points)




    # for x in range((matrix.shape[0])):
    #     for y in range(matrix.shape[1])
        
    
    # for element in range(len(matrix.shape[1])):
    #     if element >= matrix
        
saddle_points([[9, 8, 7], [5, 3, 2]])