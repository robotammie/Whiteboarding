def print_diagonals(arr):
    """
    Print out the diagonals (top-right to bottom-left) of a given 2-D array

    >>> arr = [[9, 3, 2, 4], [8, 6, 1, 2], [5, 5, 6, 7], [1, 2, 8, 4]]
    >>> print_diagonals(arr)
    9 
    3 8 
    2 6 5 
    4 1 5 1 
    2 6 2 
    7 8 
    4 


    >>> arr = [[9, 3,], [8, 6], [5, 5], [1, 2]]
    >>> print_diagonals(arr)
    9 
    3 8 
    6 5 
    5 1 
    2 

    >>> arr = [[9, 3, 2, 4], [8, 6, 1, 2]]
    >>> print_diagonals(arr)
    9 
    3 8 
    2 6 
    4 1 
    2 

    """
                  # number of diagonals = len + witdh -1
                  # (top left corner should count only once)
    for i in range((len(arr) + len(arr[0])) - 1):

        diag = ""

        # j = which row we should start on
        if i < len(arr[0]):
            j = 0
        else:
            j = i - (len(arr[0]) - 1)


        while i - j >= 0 and j < len(arr):

            if i - j < len(arr):
                diag += str(arr[j][i - j]) + " "

            j += 1

        print diag


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED!\n"
