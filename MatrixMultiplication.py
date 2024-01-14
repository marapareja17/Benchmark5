from mrjob.job import MRJob
import time

class MatrixMultiplication(MRJob):

    def configure_args(self):
        super(MatrixMultiplication, self).configure_args()
        self.add_passthru_arg('--rowsA', type=int, help='Number of rows in Matrix A')
        self.add_passthru_arg('--colsB', type=int, help='Number of columns in Matrix B')

    def mapper(self, _, line):
        matrix, i, j, value = line.split(',')
        i, j, value = int(i), int(j), float(value)

        range_to_iterate = range(self.options.colsB) if matrix == 'A' else range(self.options.rowsA)
        for k in range_to_iterate:
            yield ((i, k) if matrix == 'A' else (k, j)), (j, value)

    def reducer(self, key, values):
        result = sum(x * y for _, x in values for _, y in values if x != y)
        yield key, result

if __name__ == '__main__':
    start_time = time.time()
    MatrixMultiplication.run()
    end_time = time.time()
    print("Tiempo de Ejecución: {:.2f} segundos".format(end_time - start_time))
