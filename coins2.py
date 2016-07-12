

"""
For example:

    >>> coins2(20, [5, 10])
    5

    >>> coins2(0, [10, 1])
    1

"""


def coins2(value, denominations):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """
    # print "checking" + str(value)

    if value == 0:
        return 1

    if value < 0:
        return 0

    possible = 0

    for denom in denominations:
        possible += coins2(value - denom, denominations)
        # print possible

    return possible


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAN TAKE THAT TO THE BANK!\n"
