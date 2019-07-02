import numpy as np

def saddle_points(matrix):

    matrix = np.asarray(matrix)
    print(matrix.shape[0])
    print(matrix)
    print(matrix[2])
    print(matrix[:,0])
    print(max(matrix[0]))
    answers = []
    count = 0
    print(max(matrix[3//3]))
    print(min(matrix[:,0]))
    for x in range(len(matrix)):
        for y in matrix[x]:

            # print(np.where(matrix == y))
            if y == max(matrix[count//3]) and y == min(matrix[:,count%3]):
                answers.append(y)
            count += 1   
    print(answers)

saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]])