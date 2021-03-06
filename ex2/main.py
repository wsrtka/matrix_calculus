from optparse import OptionParser
from time import time

from matplotlib import pyplot as plt

from ex1.matrix import strassenR
from common import (
    generate_matrice,
    print_matrix,
)
from ex2.inverse import inverse


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
        inverse.counter = 0
        strassenR.counter = 0

        for i in range(2, n, 2):
            A = generate_matrice(i)

            start = time()

            C = inverse(A, l)

            total = time() - start
            times.append(total)

        plt.plot(range(2, n, 2), times)
        plt.plot(range(2, n, 2), [(n ** 2) / 12500 for n in range(2, n, 2)])
        plt.title("Czas wykonania programu w zalezności od wielkości macierzy.")
        plt.xlabel("Wielkość macierzy")
        plt.ylabel("Czas [ms]")
        plt.show()
    else:
        adds = []
        subs = []
        times = []

        for i in range(2, n, 2):
            A = generate_matrice(i)
            inverse.counter = 0
            strassenR.counter = 0
            C = inverse(A, l)
            adds.append(strassenR.counter * 12)
            subs.append(strassenR.counter * 6 + inverse.counter * 8)
            times.append(strassenR.counter * 7 + inverse.counter * 16)

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
