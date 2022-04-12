"""Main module for running matrix algorithms."""

from optparse import OptionParser
from time import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from common import generate_matrice, print_matrix
from factorization import lu, get_determinant, get_eigenvalues
from ex2.inverse import inverse
from ex1.matrix import strassenR


def main():
    """Test matrix LU factorization methods for given matrix sizes."""
    parser = OptionParser()
    parser.add_option(
        "-l",
        dest="l",
        default=8,
        help="Minimum size of matrice for which the Strassen algorithm will be used.",
        metavar="l",
    )
    parser.add_option(
        "-n",
        dest="n",
        default=128,
        help="Maximum matrice size for tests if measuring time. Matrix size otherwise.",
        metavar="n",
    )
    parser.add_option(
        "-t",
        dest="t",
        action="store_true",
        help="Specify whether we are measuring time or flops.",
        metavar="t",
    )
    options, args = parser.parse_args()

    l = int(options.l)
    n = int(options.n)
    t = bool(options.t)

    if t:
        times = []
        inverse.counter = 0
        strassenR.counter = 0
        lu.counter = 0

        for i in range(2, n, 2):
            A = generate_matrice(i)

            start = time()

            L, U = lu(A, l)

            total = time() - start
            times.append(total)
            print("\n\n\n" + 25 * "=" + "A MATRIX" + 25 * "=")
            print_matrix(A)
            print("\n\n\n" + 25 * "=" + "L MATRIX" + 25 * "=")
            print_matrix(L)
            print("\n\n\n" + 25 * "=" + "U MATRIX" + 25 * "=")
            print_matrix(U)

        plt.scatter(range(2, n, 2), times)
        plt.title("Czas wykonania programu w zalezności od wielkości macierzy.")
        plt.xlabel("Wielkość macierzy")
        plt.ylabel("Czas [ms]")
        plt.show()
    else:
        adds = []
        subs = []
        times = []
        determinants = []
        eigenvalues = []

        for i in range(2, n, 2):
            A = generate_matrice(i)
            inverse.counter = 0
            strassenR.counter = 0
            lu.counter = 0
            L, U = lu(A, l)
            adds.append(strassenR.counter * 12)
            subs.append(strassenR.counter * 6 + inverse.counter * 8 + lu.counter)
            times.append(strassenR.counter * 7 + inverse.counter * 16 + lu.counter * 5)
            if i < 32:
                determinants.append((get_determinant(L, U), np.linalg.det(A)))
                eigenvalues.append((get_eigenvalues(U), np.linalg.eig(A)))

        print(all(i == j for i, j in determinants))
        print(all(all(e == f for e, f in es) for es in eigenvalues))

        plt.plot(range(2, n, 2), adds)
        plt.title("Liczba operacji dodawania w zalezności od wielkości macierzy.")
        plt.xlabel("Wielkość macierzy")
        plt.ylabel("Liczba operacji")
        plt.show()

        plt.plot(range(2, n, 2), subs)
        plt.title("Liczba operacji odejmowania w zalezności od wielkości macierzy.")
        plt.xlabel("Wielkość macierzy")
        plt.ylabel("Liczba operacji")
        plt.show()

        plt.plot(range(2, n, 2), times)
        plt.title("Liczba operacji mnozenia w zalezności od wielkości macierzy.")
        plt.xlabel("Wielkość macierzy")
        plt.ylabel("Liczba operacji")
        plt.show()


if __name__ == "__main__":
    main()
