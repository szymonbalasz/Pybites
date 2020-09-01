class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        zip_other = list(zip(*other.values))
        matrix = [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
                   for col_b in zip_other] for row_a in self.values]
        return Matrix(matrix)

    def __rmatmul__(self, other):
        zip_other = list(zip(*other.values))
        matrix = [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
                   for col_b in zip_other] for row_a in self.values]
        return Matrix(matrix)

    def __imatmul__(self, other):
        zip_other = list(zip(*other.values))
        matrix = [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
                   for col_b in zip_other] for row_a in self.values]
        self.values = matrix
        return self
