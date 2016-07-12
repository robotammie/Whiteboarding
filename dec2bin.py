"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin_backwards(0)
    '0'

    >>> dec2bin_backwards(1)
    '1'

    >>> dec2bin_backwards(2)
    '10'

    >>> dec2bin_backwards(4)
    '100'

    >>> dec2bin_backwards(15)
    '1111'

For example, using our alternate solution::

    >>> dec2bin_forwards(0)
    '0'

    >>> dec2bin_forwards(1)
    '1'

    >>> dec2bin_forwards(2)
    '10'

    >>> dec2bin_forwards(4)
    '100'

    >>> dec2bin_forwards(15)
    '1111'

"""

import math


def dec2bin_forwards(num):
    """Convert a decimal number to binary representation."""

    if num == 0:
        return '0'

    new_num = num
    binary = ''
    i = 1

    while new_num:
        # print new_num
        if new_num % 2 ** i == 0:
            val = 0
        else:
            val = 1
            new_num -= 2 ** (i - 1)

        binary = str(val) + binary

        i += 1
        # print new_num

    return binary


def dec2bin_backwards(num):
    """Convert a decimal number to binary representation."""

    return dec2bin_forwards(num)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
