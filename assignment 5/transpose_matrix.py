
def transpose_matrix(matrix):
    # Transpose the matrix
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed = transpose_matrix(matrix)
    print("Transposed Matrix:", transposed)

if __name__ == "__main__":
    main()
