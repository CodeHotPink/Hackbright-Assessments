"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   - capsulates your code. Keeps all codes pertaining to the class together
   - inheritance. decreases amount of duplicate code. You don't have to retype the same code over & over again for different instances of the class.
   - ability to create methods/functions specifically for your classes

2. What is a class?
   - a set of objects with attributes & methods/functions that are specifically for them

3. What is a method?
   - executable code specifically for class objects

4. What is an instance in object orientation?
   - the 'child' of the class (parent). an object under a class. If there was an animal class, when you create an animal, i.e. a chicken, a chicken would be under animal class. It would inherit all the attributes of the animal.

5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   - class attribute is what the instance inherits. instance attribute is special to that instance. the animal class would have health & lays eggs attributes. for chickens you could create an egg color attribute to pass on to the chicken instances since chickens lay different colored eggs.

"""


# Part 2: Road Class
# #############################################################################

# Create your Road class here
class Road(object):
  """ Specifications of roads """
  def __init__(self, num_of_lanes=2, speed_limit=25):
    self.num_lanes = num_of_lanes
    self.speed_limit = speed_limit

# Instantiate Road objects here
road_1 = Road(4, 60)
road_2 = Road()

# Part 3: Update Password
# #############################################################################
class User(object):
    """A user object."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # write the update_password method here
    def update_password(self, current_password, new_password):
      if self.password == current_password:
        self.password = new_password
      else:
        print("Invalid password")

# Part 4: Build a Library
# #############################################################################
class Library(object):
    """ tracks book objects """
    books = []

    def add_book(self, book_title, book_author):
      book_title = Book(book_title, book_author)
      self.books.append(book_title)

    def find_books_by_author(self, book_author):
      books_by_author = []
      for book in self.books:
        if book.author == book_author:
          books_by_author.append(book)
      return books_by_author


class Book(Library):
    """A Book object."""

    def __init__(self, title, author):
        self.title = title
        self.author = author


# Part 5: Rectangles
# #############################################################################

class Rectangle(object):
    """A rectangle object."""

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the rectangle's area (length * width)."""
        return self.length * self.width


class Square(Rectangle):
    """ object from rectangle """

    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def calculate_area(self):
        """ validates & return square's area """
        if self.length == self.width:
          area = super().calculate_area()
          return area
        else:
          print("Invalid Square")
