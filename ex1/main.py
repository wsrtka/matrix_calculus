"""Main module for running matrix algorithms."""

from optparse import OptionParser
from time import time

import matplotlib.pyplot as plt

from utils import generate_matrice, print_matrix
from matrix import strassenR


def main():
    """Test matrix multiplication methods for given matrix sizes.
    """
    parser = OptionParser()
    parser.add_option(
        '-l',
        dest='l',
        default=8,
        help='Minimum size of matrice for which the Strassen algorithm will be used.',
        metavar='l'
    )
    parser.add_option(
        '-n',
        dest='n',
        default=128,
        help='Maximum matrice size for tests if measuring time. Matrix size otherwise.',
        metavar='n'
    )
    parser.add_option(
        '-t',
        dest='t',
        action='store_true',
        help='Specify whether we are measuring time or flops.',
        metavar='t'
    )
    options, args = parser.parse_args()

    l = int(options.l)
    n = int(options.n)
    t = bool(options.t)

    if t:
        times = []

        for i in range(2, n, 2):
            A = generate_matrice(i)
            B = generate_matrice(i)

            start = time()
            
            C = strassenR(A, B, l)
            
            total = time() - start
            times.append(total)

            print_matrix(C)
        
        plt.scatter(range(2, n, 2), times)
        plt.title('Czas wykonania programu w zalezności od wielkości macierzy.')
        plt.xlabel('Wieklość macierzy')
        plt.ylabel('Czas [ms]')
        plt.show()
    else:
        A = generate_matrice(n)
        B = generate_matrice(n)
        C = strassenR(A, B, l)


if __name__ == '__main__':
    main()
