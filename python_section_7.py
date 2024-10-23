import numpy as np

def rotate_and_transform(matrix):
    n = len(matrix)

  
    rotated_matrix = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]

  
    final_matrix = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
          
            row_sum = sum(rotated_matrix[i]) - rotated_matrix[i][j]
            col_sum = sum(rotated_matrix[k][j] for k in range(n)) - rotated_matrix[i][j]
            final_matrix[i][j] = row_sum + col_sum

    return final_matrix


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

final_matrix = rotate_and_transform(matrix)
for row in final_matrix:
    print(row)
