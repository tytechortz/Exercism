class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = []
        self.string = matrix_string.splitlines()
        for i in self.string:
            self.matrix.append(i.split(' '))

        self.matrix = [[int(j) for j in k] for k in self.matrix]
       

        # self.matrix.split()
        # print(self.string[0])
        print(self.matrix)



    def row(self, index):
        # print(self.matrix[index-1])
        answer = []
        for i in self.matrix[index-1].split():
            answer.append(int(i))
        # print(answer)
        return answer
        

    def column(self, index):
        answer = []
        # for i in self.matrix[:,index-1].split():
        #     answer.append(i)
        print(self.matrix)

m = Matrix("1 2 3\n4 5 6\n7 8 9\n18 7 6")
# m.column(3)
