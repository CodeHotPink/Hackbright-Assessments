"""
Skills function assessment.

Please read the instructions first. Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.
# NOTE FROM MARCELLA: What is a function signature? The return statement(s)?

#    (a) Write a function that takes a town name as a string and returns
#        `True` if it is your hometown, and `False` otherwise.
def is_hometown_the_same(hometown):
    """ If hometown input matches personal hometown, return true."""
    
    personal_hometown = "El Dorado"
    if hometown.title() == personal_hometown:
        return True
    else:
        return False

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.
def create_full_name(first_name,last_name):
    """ Concatenates first & last name to return full name"""
    
    return("{} {}".format(first_name,last_name))

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.
def greeting_for_hometown(hometown, first_name, last_name):
    """ Create greeting based off their hometown & using their full name ."""
    
    full_name = create_full_name(first_name,last_name)
    if is_hometown_the_same(hometown) is True:
        print("Howdy, {}, we're from the same place!".format(full_name))
    else:
        print("Hi, {}, I'd like to visit {}!".format(full_name,hometown))

greeting_for_hometown("el dorado","J.P.","Harrah")

###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry",
#        "blackberry", or "currant."
def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """
    
    berries = ["strawberry", "raspberry", "blackberry", "currant"]
    if fruit.lower() in berries:
        return True
    else:
        return False

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.
def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """
    
    item_shipping_cost = is_berry(fruit)
    if item_shipping_cost is True:
        return 0
    else:
        return 5

#    (c) Make a function that takes in a fruit name and a list of fruits. It should
#        return a new list containing the elements of the input list, along with
#        given fruit, which should be at the end of the new list.
def append_to_list(lst, fruit):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list(['banana', 'apple', 'blackberry'], 'dragonfruit')
    ['banana', 'apple', 'blackberry', 'dragonfruit']

    >>> fruits = ['banana', 'apple', 'blackberry']
    >>> append_to_list(fruits, 'dragonfruit')
    ['banana', 'apple', 'blackberry', 'dragonfruit']
    >>> fruits
    ['banana', 'apple', 'blackberry']

    """
    
    updated_lst = []
    updated_lst += lst
    updated_lst.append(fruit)
    return updated_lst

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price of $100 or less and $3 for items over $100. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.
def validate_if_price_is_digit_only(price):
# NOTE FROM MARCELLA: Not sure of how to format float to only show 2 digits
# from right side of decimal point
    """ Validates price entry."""
    
    while True:
        try:
            float(price)
            return price
        except ValueError:
            print("Enter price in digits.")
            price = input()

def validate_state_abbreviation(state_abbreviation):
    """ Validates state abbreviation."""
    
    states = ["AK", "AL", "AZ", "AR", "CA","CO","CT","DE","FL","GA","HI","ID",
    "IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE",
    "NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN",
    "TX","UT","VT","VA","WA","WV","WI","WY"]
    while state_abbreviation.upper() not in states:
        print("Enter valid two letter state abbreviation.")
        state_abbreviation = input().upper()
    return state_abbreviation

def validate_two_digit_decimal_for_tax(two_digit_decimal_tax):
    """ Validates if tax contains two digit decimal"""
    
    while True:
        try:
            float(two_digit_decimal_tax)
            while two_digit_decimal_tax > 1:
                print("Enter tax percentage. Example: 5% = ""0.5"".")
                two_digit_decimal_tax = input()
            return two_digit_decimal_tax
        except ValueError:
            print("Enter tax percentage as decimal. Example: 5% = ""0.5"".")
            two_digit_decimal_tax = input()
            
def get_total_amount(price, two_digit_decimal_tax = 0.05):
    return price + (price * two_digit_decimal_tax)

def calculate_price(price,state_abbreviation,two_digit_decimal_tax = .05):
#  NOTE FROM MARCELLA: Had to search up how to declare default argument/parameter, I forgot how
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """
    
    price = validate_if_price_is_digit_only(price)
    state_abbreviation = validate_state_abbreviation(state_abbreviation)
    total_amount = get_total_amount(price,two_digit_decimal_tax = 0.05)
    
    if state_abbreviation == "CA":
        total_amount += (total_amount * 0.03)
        return total_amount
        # CA recycling fee
        
    if state_abbreviation == "PA":
        total_amount += 2
        return total_amount
        # PA highway safety fee
        
    if state_abbreviation == "MA":
        if price > 100:
            total_amount += 3
            return total_amount
        else:
            total_amount += 1
            return total_amount
            # MA Commonwealth Fund fee based off base price
    else:
        return total_amount

###############################################################################

# PART THREE

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.
def create_new_list(original_list,*args):
    """ Takes in list, along with arguments to create a new list. """
    new_list = original_list[:]
    for entry in args:
        new_list.append(entry)
    return new_list

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.
def multiply_word(word):
    word *= 3
    return word
def create_tuple_of_multiplied_word(word):
    multiplied_word = multiply_word(word)
    print(tuple([word, multiplied_word]))
    

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.
#
if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
