var1 = ("Hello") # string
var2 = ("Hello",) # tuple

# accessing tuple elements using indexing
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")

print(letters[0])   # prints "p" 
print(letters[5])   # prints "a"
print(letters[-3])   # prints 'm'

my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # prints 2
print(my_tuple.index('l'))  # prints 3



"""Advantages of Tuple over List in Python

Since tuples are quite similar to lists, both of them are used in similar situations.

However, there are certain advantages of implementing a tuple over a list:

    We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
    Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
    Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
    If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.
"""

"""Tuples operation has smaller size than that of list, which makes it a bit faster but not that much to mention about until you have a huge number of elements."""