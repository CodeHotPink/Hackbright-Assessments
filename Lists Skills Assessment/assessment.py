
"""List Assessment
Edit the functions until all of the doctests pass when
you run this file.
"""


def print_indices(items):
    """Print each item in the list, followed by its index. Do this without
    using a "counting variable" --- that is, don't do something like this::
        count = 0
        for item in list:
            print(count)
            count = count + 1
    Output should look like this::
        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        Toyota 0
        Jeep 1
        Volvo 2
        >>> print_indices(["Toyota", "Jeep", "Toyota", "Volvo"])
        Toyota 0
        Jeep 1
        Toyota 2
        Volvo 3

    """
    for item_index, item in enumerate(items):
        print(item, item_index)

def words_in_common(words1, words2):
    """Find words in common.
    Given 2 lists of words, return the words that are in common
    between the two, sorted alphabetically.
    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists).
    For example::
        >>> common_words = words_in_common(
        ...    ["Python", "Ruby", "R", "C++", "Haskell"],
        ...    ["Lizard", "Turtle", "Python"]
        ...    )
        >>> print (common_words)
        ['Python']

    The returned list should not have any duplicates::
        >>> common_words = words_in_common(
        ...    ["cheese", "bagel", "cake", "cheese"],
        ...    ["hummus", "cheese", "beets", "kale", "bagel", "cake"]
        ... )
        >>> print (common_words)
        ['bagel', 'cake', 'cheese']

    If there are no words in common, return an empty list::
        >>> common_words = words_in_common(
        ... ["lamb", "chili", "cheese"],
        ... ["cake", "ice cream"]
        ... )
        >>> print (common_words)
        []

    If a duplicate exists in the original lists, the result will
    contain the value only once::
        >>> common_words = words_in_common(
        ...    ["Python", "Ruby", "R", "C++", "Haskell"],
        ...    ["Lizard", "Turtle", "Python", "Python"]
        ...    )
        >>> print (common_words)
        ['Python']
    """
    words_in_common = set()
    for word in words1:
        if word in words2:
            words_in_common.add(word)
    return sorted(words_in_common)


def every_other_item(items):
    """Return every other item in `items`, starting at first item.
    For example::
       >>> alternating_items = every_other_item(['a', 'b', 'c', 'd', 'e', 'f'])
       >>> print (alternating_items)
       ['a', 'c', 'e']
       >>> alternating_items = every_other_item(["pickle", "pickle", "juice", "pickle", "juice", "pop"])
       >>> print (alternating_items)
       ['pickle', 'juice', 'juice']
       >>> alternating_items = every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       >>> print (alternating_items)
       ['you', 'are', 'good', 'at', 'code']
    """
    return items[::2]


def smallest_n_items(items, n):
    """Return the `n` smallest integers in list, in descending order.
    You can assume that `n` will be less than the length of the list.
    For example::
    >>> smallest = smallest_n_items([2, 6006, 700, 42, 6, 59], 3)
    >>> print (smallest)
    [42, 6, 2]

    It should work when `n` is 0::
    >>> smallest = smallest_n_items([3, 4, 5], 0)
    >>> print (smallest)
    []

    If there are duplicates in the list, they should be counted
    separately::
    >>> smallest = smallest_n_items([3, 1, 3, 2, 1, 1], 2)
    >>> print (smallest)
    [1, 1]

    """
    sorted_items = sorted(items)
    if n != 0:
        sorted_items = sorted_items[0:n]
        return sorted_items[::-1]
    return []
    #Is there a shorter way to code this?


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")
