import numpy as np

def saddle_points(matrix):
    saddle_points = []

    matrix = np.asarray(matrix)
    # print(len(matrix))
    # print(matrix.shape)
    # print(matrix[1,1])
    # print(matrix[0])
    # print(matrix[:,0])
    if len(matrix) == 0:
        print([dict()])
    elif len(matrix) == 1:
        print([{"row":matrix[0], "column":matrix[0]}])
    else:
        for x in range(len(matrix)):
            for y in range(matrix.shape[1]):
                if matrix[x][y] >= max(matrix[x]) and matrix[x][y] == min(matrix[:,y]):
                    saddle_points.append({"row": x+1, "column": y+1})
        print(saddle_points)

    # for points in saddle_points:





    # for x in range((matrix.shape[0])):
    #     for y in range(matrix.shape[1])
        
    
    # for element in range(len(matrix.shape[1])):
    #     if element >= matrix
        
saddle_points([[4, 5, 4], [3, 5, 5], [1, 5, 4]])