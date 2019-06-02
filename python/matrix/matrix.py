class Matrix(object):
    def __init__(self, matrix_string):
        # # self.matrix = matrix_string.split()
        # self.matrix = matrix_string.split('\n')
        # # for i in self.matrix: 
        # #     ",".join(self.matrix)
        # print(self.matrix)
        self.matrix = matrix_string.splitlines()

    def row(self, index):
        # print(self.matrix[index-1])
        answer = []
        for i in self.matrix[index-1].split():
            answer.append(int(i))
        # print(answer)
        return answer
        

    def column(self, index):
        pass

# m = Matrix("1 2 3\n4 5 6\n7 8 9\n18 7 6")
# m.row(3)