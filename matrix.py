class Matrix:
    def __init__(self, rows, cols, data):
        self.rows = rows
        self.cols = cols
        self.data = data

    def size(self):
        return self.rows, self.cols

    def get_value(self, i, j):
        return self.data[i][j]

    def set_value(self, i, j, value):
        self.data[i][j] = value
