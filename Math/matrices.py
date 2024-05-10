import math

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def matrix_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        determinant = 0
        for j in range(len(matrix[0])):
            determinant += ((-1) ** j) * matrix[0][j] * matrix_determinant(matrix_minor(matrix, 0, j))
        return determinant

def matrix_inverse(matrix):
    determinant = matrix_determinant(matrix)
    if determinant == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    
    n = len(matrix)
    adjugate = []
    for i in range(n):
        adjugate_row = []
        for j in range(n):
            minor = matrix_minor(matrix, i, j)
            cofactor = ((-1) ** (i+j)) * matrix_determinant(minor)
            adjugate_row.append(cofactor)
        adjugate.append(adjugate_row)
    
    adjugate = transpose(adjugate)
    inverse = [[adjugate[i][j] / determinant for j in range(n)] for i in range(n)]
    
    return inverse

def matrix_product(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must be equal to the number of rows in B")
    
    m = len(A)
    n = len(B[0])
    p = len(B)
    
    # Initialize result matrix
    C = [[0 for _ in range(n)] for _ in range(m)]
    
    # Compute product
    for i in range(m):
        for j in range(n):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def matrix_sum(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for addition")
    
    m = len(A)
    n = len(A[0])
    
    # Initialize result matrix
    C = [[0 for _ in range(n)] for _ in range(m)]
    
    # Compute sum
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    
    return C

def matrix_subtraction(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction")
    
    m = len(A)
    n = len(A[0])
    
    # Initialize result matrix
    C = [[0 for _ in range(n)] for _ in range(m)]
    
    # Compute subtraction
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    
    return C

def matrix_elementwise_product(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions for element-wise product")
    
    m = len(A)
    n = len(A[0])
    
    # Initialize result matrix
    C = [[0 for _ in range(n)] for _ in range(m)]
    
    # Compute element-wise product
    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] * B[i][j]
    
    return C

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Test the functions with valid input dimensions
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

print(f"For matrices {A} X {B}")
try:
    print("\nMatrix Product:")
    product_result = matrix_product(A, B)
    print_matrix(product_result)
    with open("matrix_product_result.txt", "w") as file:
        for row in product_result:
            file.write(" ".join(map(str, row)) + "\n")
except ValueError as e:
    print("Matrix Product Error:", e)

try:
    print("\nMatrix Sum:")
    sum_result = matrix_sum(A, B)
    print_matrix(sum_result)
    with open("matrix_sum_result.txt", "w") as file:
        for row in sum_result:
            file.write(" ".join(map(str, row)) + "\n")
except ValueError as e:
    print("Matrix Sum Error:", e)

try:
    print("\nMatrix Subtraction:")
    subtraction_result = matrix_subtraction(A, B)
    print_matrix(subtraction_result)
    with open("matrix_subtraction_result.txt", "w") as file:
        for row in subtraction_result:
            file.write(" ".join(map(str, row)) + "\n")
except ValueError as e:
    print("Matrix Subtraction Error:", e)

try:
    print("\nMatrix Element-wise Product:")
    elementwise_product_result = matrix_elementwise_product(A, B)
    print_matrix(elementwise_product_result)
    with open("matrix_elementwise_product_result.txt", "w") as file:
        for row in elementwise_product_result:
            file.write(" ".join(map(str, row)) + "\n")
except ValueError as e:
    print("Matrix Element-wise Product Error:", e)

# Matrix inversion test

matrix_to_invert = [[1, 0],
                    [0, 1]]

print("\nMatrix to invert:")
print_matrix(matrix_to_invert)

try:
    print("\nMatrix Inversion:")
    inverse_matrix = matrix_inverse(matrix_to_invert)
    print("Inverse of the matrix:")
    for row in inverse_matrix:
        print(row)
except ValueError as e:
    print("Matrix Inversion Error:", e)
