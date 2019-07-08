import numpy as np

def saddle_points(matrix):

    matrix = np.asarray(matrix)
    print(matrix.shape)
    # print(matrix)
    # print(matrix[2])
    # print(matrix[:,0])
    # print(max(matrix[0]))
    answers = []
    count = 0
    # print(max(matrix[3//3]))
    # print(min(matrix[:,0]))
    for x in range(len(matrix)):
        for y in matrix[x]:

            # print(np.where(matrix == y))
            if y == max(matrix[count//matrix.shape[0]]) and y == min(matrix[:,count % matrix.shape[0]]):
                answers.append({"row": count//matrix.shape[0]+1, "column": count % matrix.shape[1]+1})
            count += 1   
    print(answers)
    return answers

saddle_points([[3, 1, 3], [3, 2, 4]])