import numpy as np

def saddle_points(matrix):
    m = np.array(matrix)
    sp = []
    rows = m.shape[0]
    cols = m.shape[1]
    print(m)
    for x in range(0, rows):
        for y in range(0, cols):
            print(m[x,y])
    



saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]])