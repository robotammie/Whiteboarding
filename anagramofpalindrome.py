"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""
"""
    initialize dict {letter:instances}
    iterate through string
        add letter to dict/iterate letter in dict
    initialize odds = 0
    iterate through dict
        if val %2 != 0
            if odds > 0 return false
            odds += 1
"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    letter_instances = {}

    for char in word:
        letter_instances[char] = letter_instances.get(char, 0) + 1

    odds = 0
    for char in letter_instances:
        if letter_instances[char] % 2 != 0:
            if odds > 0:
                return False
            odds += 1

    return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
