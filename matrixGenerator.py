
size_512 = 1024

matrix_data_512_A = [[i * j for j in range(size_512)] for i in range(size_512)]

matrix_lines_512_A = [f"A,{i},{j},{matrix_data_512_A[i][j]}" for i in range(size_512) for j in range(size_512)]

matrix_content_512_A = "\n".join(matrix_lines_512_A)

matrix_file_512_A_path = 'C:\\Users\\marap\\OneDrive\\Documentos\\ProyectosVisual\\MapReduce\\matrixes\\matriz_1024_B.txt'

with open(matrix_file_512_A_path, 'w') as file:
    file.write(matrix_content_512_A)

matrix_file_512_A_path
