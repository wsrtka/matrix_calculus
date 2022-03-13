"""Module containing matrix multiplication algorithms."""


def read(filename):
    lines = open(filename).read().splitlines()
    A = []
    B = []
    matrix = A
    for line in lines:
        if line != "":
            matrix.append([int(el) for el in line.split("\t")])
        else:
            matrix = B
    return A, B


def print_matrix(matrix):
    for line in matrix:
        print("\t".join(map(str, line)))


def ikj_matrix_product(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def add(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C
