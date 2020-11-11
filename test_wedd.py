from main import wedd




def main():
    """
    main function to run algorithm
    :return:
    >>> wedd(6,[(1, 2), (2, 4), (1, 3), (7, 5), (8, 10)])
    12
    >>> wedd(6,[(1, 2), (2, 4), (3, 5)])
    4
    >>> wedd(6,[(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)])
    6
    """


if __name__ == '__main__':

    import doctest

    doctest.testmod(verbose=True)
