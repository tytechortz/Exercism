import numpy as np

def saddle_points(matrix):
    m = np.array(matrix)
    sp = []
    rows = m.shape[0]
    cols = m.shape[1]
    print(m[1,0])
    # print(m[:,1])
    for x in range(0, rows):
        for y in range(0, cols):
            if m[x,y] == max(m[x,:]) and m[x,y] == min(m[:,y]):
                sp.append((x+1,y+1))
    print(sp)
    



saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]])