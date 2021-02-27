
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


def matrix():
    while True:
        print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit""")
        choice = int(input("Your choice:"))
        if choice == 1:
            add_matrices()
        elif choice == 2:
            multiply_matrix_by_a_constant()
        elif choice == 3:
            multiply_matrices()
        elif choice == 0:
            break
matrix()