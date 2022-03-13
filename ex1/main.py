"""Main module for running matrix algorithms."""

from optparse import OptionParser


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

    for i in range(2, n, 2):
        A = ...


if __name__ == '__main__':
    main()
