class Matrix:
    def __init__(self, matrix_string):
        try:
            self.matrix = list()
            for i in matrix_string.split('\n'):
                self.matrix.append([int(j) for j in i.split()])
        except:
            print('Invalid matrix string input')

    def row(self, index):
        return self.matrix[index - 1].copy()

    def column(self, index):
        return [i[index - 1] for i in self.matrix]