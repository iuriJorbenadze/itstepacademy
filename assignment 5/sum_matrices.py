
def sum_matrices(matrix1, matrix2):
    # Ensure both matrices have the same dimensions
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise ValueError("Matrices must have the same dimensions")

    # Sum the elements of the matrices
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def main():
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    result = sum_matrices(matrix1, matrix2)
    print("Sum of matrices:", result)

if __name__ == "__main__":
    main()
