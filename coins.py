"""Calculate possible change from combinations of dimes and pennies.

Given an infinite supply of dimes and pennies, find the different
amounts of change can be created with exact `num_coins` coins?

For example, when num_coins = 3, you can create:

    3 = penny + penny + penny
   12 = dime + penny + penny
   21 = dime + dime + penny
   30 = dime + dime + dime

For example:

    >>> coins(0) == {0}
    True

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True

    >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
    True
"""


# def coins(num_coins):
#     """Find change from combinations of `num_coins` of dimes and pennies.

#     This should return a set of the unique amounts of change possible.
#     """

#     values = set([])

#     for i in range(num_coins + 1):
#         values.add(i + 10 * (num_coins - i))

#     return values


def coins(num_coins, denominations=[1, 10]):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """

    if num_coins == 0:
        return set([0])

    vals = set()

    for value in coins(num_coins - 1):
        for denom in denominations:
            vals.add(value + denom)

    return vals


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAN TAKE THAT TO THE BANK!\n"
