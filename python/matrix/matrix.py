class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = []
        self.string = matrix_string.splitlines()
        for i in self.string:
            self.matrix.append(i.split(' '))

        self.matrix = [[int(j) for j in k] for k in self.matrix]
       
    def row(self, index):
        answer = []
        for i in self.matrix[index-1]:
            answer.append(int(i))
        return answer
        

    def column(self, index):
        return [row[index-1] for row in self.matrix]

m = Matrix("1")
m.row(3)
m.column(1)
