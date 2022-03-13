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
        help='Maximum matrice size for tests.',
        metavar='n'
    )
    options, args = parser.parse_args()

    l = int(options.l)
    n = int(options.n)

    times = []
    flops = []

    for i in range(2, n, 2):
        A = generate_matrice(i)
        B = generate_matrice(i)

        start = time()
        
        C = strassenR(A, B, l)
        
        total = time() - start
        times.append(total)

        print_matrix(A)
        print('*')
        print_matrix(B)
        print('=')
        print_matrix(C)
    
    plt.scatter(range(2, n, 2), times)
    plt.title('Czas wykonania programu w zalezności od wielkości macierzy.')
    plt.xlabel('Wieklość macierzy')
    plt.ylabel('Czas [ms]')
    plt.plot()


if __name__ == '__main__':
    main()
