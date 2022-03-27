from optparse import OptionParser
from time import time

from matplotlib import pyplot as plt

from matrix_calculus.ex1.matrix import strassenR
from matrix_calculus.common import (
    generate_matrice,
    print_matrix,
)
from matrix_calculus.ex2.inverse import inverse


def main():
    """Test matrix multiplication methods for given matrix sizes."""
    parser = OptionParser()
    parser.add_option(
        "-l",
        dest="l",
        default=10,
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

        for i in range(2, n, 2):
            A = generate_matrice(i)

            start = time()

            C = inverse(A, l)

            total = time() - start
            times.append(total)

        plt.plot(range(2, n, 2), times)
        plt.title("Czas wykonania programu w zalezności od wielkości macierzy.")
        plt.xlabel("Wielkość macierzy")
        plt.ylabel("Czas [ms]")
        plt.show()
    else:
        A = generate_matrice(n)
        C = inverse(A, l)
        print_matrix(C)


if __name__ == "__main__":
    main()