def saddle_points(matrix):
    if not all([len(r) == len(matrix[0]) for r in matrix]):
        raise ValueError('irregular matrix')

    print(enumerate(matrix))

    points = []
    for row_idx, row in enumerate(matrix):
        row_max = max(row)
    #     print(row_max)
        for col_idx, col in enumerate(row):
            col_min = min(zip(matrix)[col_idx])
        print(col_min)

    # return set(points)

saddle_points([[4, 5, 4], [3, 5, 5], [1, 5, 4]])