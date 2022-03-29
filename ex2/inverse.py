import copy
from typing import List

import numpy as np

from matrix_calculus.ex1.matrix import strassenR
from matrix_calculus.common import subtract, get_empty_matrix, get_identity_matrix


def inverse(A: List[List[float]], l: int) -> List[List[float]]:
    """Compute the inverse of a matrix using the recursive method. This method uses the Strassen algorithm for
    multiplication of large matrices.

    Args:
        A (List[List[float]]): matrix
        l (int): minimum size of matrix for which the Strassen algorithm will be used.

    Returns:
        List[List[float]]: result of multiplication.
    """
    # 8 odejmowań
    # 16 mnozen
    inverse.counter += 1
    n = len(A)

    if n == 1:
        A[0][0] = 0 if A[0][0] == 0 else A[0][0] ** -1
        return A

    # initializing the new sub-matrices
    new_size = n // 2
    a11 = get_empty_matrix(new_size)
    a12 = get_empty_matrix(new_size)
    a21 = get_empty_matrix(new_size)
    a22 = get_empty_matrix(new_size)

    # initializing the identity sub-matrices
    i11 = get_identity_matrix(new_size)
    i12 = get_empty_matrix(new_size)
    i21 = get_empty_matrix(new_size)
    i22 = get_identity_matrix(new_size)

    # dividing the matrices in 4 sub-matrices:
    for i in range(0, new_size):
        for j in range(0, new_size):
            a11[i][j] = A[i][j]  # top left
            a12[i][j] = A[i][j + new_size]  # top right
            a21[i][j] = A[i + new_size][j]  # bottom left
            a22[i][j] = A[i + new_size][j + new_size]  # bottom right

    # Step 1 - inverse of the top-left matrix
    a11_1 = inverse(a11, l)

    # Step 2 - recursively multiply all sub-matrices in the first row
    a11_new = strassenR(a11_1, a11, l)
    a12_new = strassenR(a11_1, a12, l)
    i11_new = strassenR(a11_1, i11, l)
    i12_new = strassenR(a11_1, i12, l)

    # Step 3 - from the second row subtract the new first row elements multiplied by the bot-left matrix
    a21_new = subtract(a21, strassenR(a21, a11_new, l))
    s22 = subtract(
        a22, strassenR(a21, a12_new, l)
    )  # this is the symbol used in the conspect
    i21_new = subtract(i21, strassenR(a21, i11_new, l))
    i22_new = subtract(i22, strassenR(a21, i12_new, l))

    # Step 4 - inverse of s22
    s22_1 = inverse(s22, l)

    # Step 5 - second row
    a21_new = strassenR(s22_1, a21_new, l)
    s22 = strassenR(s22_1, s22, l)
    i21_new = strassenR(s22_1, i21_new, l)
    i22_new = strassenR(s22_1, i22_new, l)

    # Step 6 - first row
    a11_1_mult_a12 = copy.deepcopy(a12_new)  # remember the original state of a12_new
    a11_new = subtract(a11_new, strassenR(a11_1_mult_a12, a11_new, l))
    a12_new = subtract(a12_new, strassenR(a11_1_mult_a12, a12_new, l))
    i11_new = subtract(i11_new, strassenR(a11_1_mult_a12, i11_new, l))
    i12_new = subtract(i12_new, strassenR(a11_1_mult_a12, i22_new, l))

    # Grouping the results obtained in a single matrix:
    C = get_empty_matrix(n)
    for i in range(n):
        for j in range(n):
            if i < new_size and j < new_size:
                C[i][j] = i11_new[i][j]
            elif i < new_size:
                C[i][j] = i12_new[i][j % new_size]
            elif j < new_size:
                C[i][j] = i21_new[i % new_size][j]
            else:
                C[i][j] = i22_new[i % new_size][j % new_size]
    return C
