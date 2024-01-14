from matrix import Matrix

class DenseMatrixMultiplier:
    @staticmethod
    def multiply(matrixA, matrixB):
        a_rows, a_cols = matrixA.size()
        b_rows, b_cols = matrixB.size()

        if a_cols != b_rows:
            raise ValueError("Matrices cannot be multiplied due to incompatibility of dimensions.")

        result = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

        for i in range(a_rows):
            for k in range(b_cols):
                aik = matrixA.get_value(i, k)
                for j in range(a_cols):
                    result[i][j] += aik * matrixB.get_value(k, j)

        return Matrix(a_rows, b_cols, result)
