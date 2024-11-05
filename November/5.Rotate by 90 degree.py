def rotate(mat):
    n = len(mat)

    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(n):
        mat[i].reverse()

def print_matrix(mat):
    for row in mat:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate(mat)
    print_matrix(mat)
