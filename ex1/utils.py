"""Module containing utility functions."""

import random


def read(filename):
    """Read two matrices seperated by empty line from file.

    Args:
        filename (str): name of the file to read

    Returns:
        tuple(List[List[int]]): two matrices
    """
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
    """Prints a matrix.

    Args:
        matrix (List[List[int]]): matrix to print.
    """
    for line in matrix:
        print("\t".join(map(str, line)))


def add(A, B):
    """Computes the elementwise sum of two matrices.

    Args:
        A (List[List[int]]): first matrice
        B (List[List[int]]): second matrice

    Returns:
        List[List[int]]: result of matrix product.
    """
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract(A, B):
    """Subtract two matrices.

    Args:
        A (List[List[int]]): first matrice
        B (List[List[int]]): second matrice

    Returns:
        List[List[int]]: result of matrix product.
    """
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C


def generate_matrice(n):
    """Generate matrice with random values.

    Args:
        n (int): Size of matrice to generate.
    """
    matrice = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]
    return matrice
