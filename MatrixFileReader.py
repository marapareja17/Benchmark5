from matrix import Matrix
from denseMatrixMultiplier import DenseMatrixMultiplier
import time

class MatrixFileReader:

    @staticmethod
    def read_matrix_from_file(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        max_row = max_col = 0
        for line in lines:
            _, i, j, _ = line.strip().split(',')
            max_row = max(max_row, int(i))
            max_col = max(max_col, int(j))

        matrix_data = [[0 for _ in range(max_col + 1)] for _ in range(max_row + 1)]

        for line in lines:
            _, i, j, value = line.strip().split(',')
            matrix_data[int(i)][int(j)] = int(value)

        return Matrix(max_row + 1, max_col + 1, matrix_data)

matrix_A = MatrixFileReader.read_matrix_from_file('matrixes/matriz_1024_A.txt')
matrix_B = MatrixFileReader.read_matrix_from_file('matrixes/matriz_1024_B.txt')

start_time = time.time()
result_matrix = DenseMatrixMultiplier.multiply(matrix_A, matrix_B)
end_time = time.time()


for row in result_matrix.data:
    print(row)

print("Tiempo de Ejecución: {:.2f} segundos".format(end_time - start_time))
