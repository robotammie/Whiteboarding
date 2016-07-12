# input: list of ints
# output: bool - if any two nums add to zero (1, -1)

"""
    make a set of all the thngs in the list

    iterate through the list
    for each num: see if reciprocal is in set
    if we finds a match - return



"""


def add_to_zero(num_list):
    num_set = set(num_list)
    for num in num_list:
        if num == 0:
            return True
        if -num in num_set:
            return True
    return False
