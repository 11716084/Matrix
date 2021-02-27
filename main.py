def input_matrix():
    # test input:
    # n, m = 2, 3
    # matrix = [[1, 2, 3], [5, 7, 11]]
    print("Enter matrix size:")
    n, m = [int(dim) for dim in input().split()]
    print("Enter matrix:")
    matrix = [[float(element) for element in input().split()] for _ in range(n)]
    return n, m, matrix
#  1. Add matrices
def add_matrices():
    m, n = list(map(int, input("Enter size of first matrix:").split()))
    a = []
    print("Enter first matrix:")
    for i in range(1, m + 1):
        b = []
        # print("{0} Row".format(i))
        z = list(map(float, input().split()))
        for j in z:
            b.append(j)
        a.append(b)

    # Second matrix
    o, p = list(map(int, input("Enter size of second matrix:").split()))
    c = []
    print("Enter second matrix:")
    for i in range(1, o + 1):
        b = []
        # print("{0} Row".format(i))
        z = list(map(float, input().split()))
        for j in z:
            b.append(j)
        c.append(b)
    if m == o and n == p:
        result = ([a[i][j] + c[i][j] for j in range
        (len(a[0]))] for i in range(len(a)))
        print("The result is:")
        print('\n'.join([' '.join(['{0:}'.format(item) for item in row])
                         for row in result]))

    else:
        print("The operation cannot be performed.")


#  2. Multiply matrix by a constant
def multiply_matrix_by_a_constant():
    m, n = list(map(int, input("Enter size of matrix:").split()))
    a = []
    for i in range(1, m + 1):
        b = []
        # print("{0} Row".format(i))
        z = list(map(float, input("Enter matrix:").split()))
        for j in z:
            b.append(j)
        a.append(b)
    c = float(input("Enter constant:"))

    result = ([a[i][j] * c for j in range
    (len(a[0]))] for i in range(len(a)))
    print("The result is:")
    print('\n'.join([' '.join(['{0:}'.format(item) for item in row])
                     for row in result]))

def multiply_matrices():
    m, n = list(map(int, input("Enter size of first matrix:").split()))
    a = []
    print("Enter first matrix:")
    for i in range(1, m + 1):
        b = []
        # print("{0} Row".format(i))
        z = list(map(float, input().split()))
        for j in z:
            b.append(j)
        a.append(b)

    # Second matrix
    o, p = list(map(int, input("Enter size of second matrix:").split()))
    c = []
    print("Enter second matrix:")
    for i in range(1, o + 1):
        b = []
        # print("{0} Row".format(i))
        z = list(map(float, input().split()))
        for j in z:
            b.append(j)
        c.append(b)

    if n == o:
        result = [[0 for row in range(p)] for col in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    result[i][j] += a[i][k] * c[k][j]
        print("The result is:")
        print('\n'.join([' '.join(['{0:}'.format(item) for item in row])
                             for row in result]))




def transpose_matrix():
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    your_choice = int(input("Your choice: "))
    n, m, matrix = input_matrix()
    if your_choice == 1:
        output_matrix = [[matrix[i][j] for i in range(n)] for j in range(m)]
    elif your_choice == 2:
        output_matrix = [[matrix[n - i - 1][m - j - 1] for i in range(n)] for j in range(m)]
    elif your_choice == 3:
        output_matrix = [[matrix[j][m - i - 1] for i in range(m)] for j in range(n)]
    else:
        output_matrix = [[matrix[n - j - 1][i] for i in range(m)] for j in range(n)]
    return output_matrix

def print_matrix(output_matrix):
    if output_matrix:
        print("The result is:")
        [print(*row) for row in output_matrix]
        print()
    else:
        print("The operation cannot be performed.")

def matrix():
    while True:
        print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit""")
        choice = int(input("Your choice:"))
        if choice == 1:
            add_matrices()
        elif choice == 2:
            multiply_matrix_by_a_constant()
        elif choice == 3:
            multiply_matrices()
        elif choice == 4:
            print_matrix(transpose_matrix())
        elif choice == 0:
            break
matrix()