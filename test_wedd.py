from main import wedd


def main():
    """
    main function to run algorithm
    :return scdfng:
    >>> wedd([(1, 2), (2, 4), (1, 3), (7, 5), (8, 10)], 5)
    12
    >>> wedd([(1, 2)],1)
    0
    >>> wedd([],0)
    0
    >>> wedd([(1, 2), (2, 4), (4, 6), (6, 7)],4)
    0
    >>> wedd([(1, 2), (2, 4), (3, 5)],3)
    4
    >>> wedd([(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)],5)
    6
    >>> wedd([(1, 2), (3, 4), (5, 6)],3)
    6
    >>> wedd([(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)],1001)
    To much families
    0
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
