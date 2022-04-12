"""Module containing matrix factorization functions."""

from common import get_empty_matrix, subtract
from ex2.inverse import inverse
from ex1.matrix import strassenR


def lu(A: list, l: int) -> tuple:
    lu.counter += 1
    n = len(A)

    if n == 1:
        if A[0][0]:
            A[0][0] = 1 / A[0][0]
        return A, A

    # initializing the new sub-matrices
    new_size = n // 2
    l11 = get_empty_matrix(new_size)
    l12 = get_empty_matrix(new_size)
    l21 = get_empty_matrix(new_size)
    l22 = get_empty_matrix(new_size)

    u11 = get_empty_matrix(new_size)
    u12 = get_empty_matrix(new_size)
    u21 = get_empty_matrix(new_size)
    u22 = get_empty_matrix(new_size)

    a11 = get_empty_matrix(new_size)
    a12 = get_empty_matrix(new_size)
    a21 = get_empty_matrix(new_size)
    a22 = get_empty_matrix(new_size)

    # dividing the matrices in 4 sub-matrices:
    for i in range(0, new_size):
        for j in range(0, new_size):
            a11[i][j] = A[i][j]  # top left
            a12[i][j] = A[i][j + new_size]  # top right
            a21[i][j] = A[i + new_size][j]  # bottom left
            a22[i][j] = A[i + new_size][j + new_size]  # bottom right

    # 1. calculate lu of upper left submatrice
    l11, u11 = lu(a11, l)

    # 2. calculate inverse of upper left upper matrix
    u11_inv = inverse(u11, l)
    
    # 3. calculate lower left lower matrix
    l21 = strassenR(a21, u11_inv, l)

    # 4. calculate inverse of upper left lower matrix
    l11_inv = inverse(l11, l)

    # 5. calculate upper right part of upper matrix
    u12 = strassenR(l11_inv, a12, l)

    # 6. calculate lower right parts of upper and lower matrices
    l22_part = strassenR(a21, u11_inv, l)
    l22_part = strassenR(l22_part, l11_inv, l)
    l22_part = strassenR(l22_part, a12, l)
    l22 = subtract(a22, l22_part)
    l22, u22 = lu(l22, l)

    # Grouping the results obtained in result matrices:
    L = get_empty_matrix(n)
    U = get_empty_matrix(n)
    for i in range(n):
        for j in range(n):
            if i < new_size and j < new_size:
                L[i][j] = l11[i][j]
                U[i][j] = u11[i][j]
            elif i < new_size:
                L[i][j] = l12[i][j % new_size]
                U[i][j] = u12[i][j % new_size]
            elif j < new_size:
                L[i][j] = l21[i % new_size][j]
                U[i][j] = u21[i % new_size][j]
            else:
                L[i][j] = l22[i % new_size][j % new_size]
                U[i][j] = u22[i % new_size][j % new_size]

    return L, U


def get_determinant(L: list, U: list) -> float:
    result = 0
    for i in range(len(L)):
        result += L[i][i] * U[i][i]
    return result


def get_eigenvalues(U: list) -> float:
    results = []
    for i in range(len(U)):
        results.append(U[i][i])
    return results
