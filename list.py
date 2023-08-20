"""In Python, a hashable object is an object that has a hash value that does not change over time. This hash value is used by dictionaries to quickly look up keys. Mutable objects cannot be hashable because their values can change, which would invalidate their hash values.This means that you cannot use mutable types, such as lists, dictionaries, and sets, as dictionary keys."""

"""
Type	     Hashable
Strings	      Yes
Numbers	      Yes
Tuples	      Yes
Frozensets	  Yes
Lists	       No
Dictionaries   No
Sets	       No
"""

"""
Mutable Objects
Lists
Dictionaries
Sets
Byte Arrays
"""
import copy
def test_func1(list1):
    print(id(list1))
    list1[0] = 23
    """same copy"""
    return list1




"""Lists are dynamic, so they can
change their size"""
"""Time Complexity Append O(1)
Insert O(n)"""
list1 = [1,2,3,4,5]
print(id(list1))

print(test_func1(list1.copy()))
list2 = copy.copy(list1)
print(test_func1(list1[:]))
list1[1]='Mohim'
print(list1)
print(list2)

"""Shallow Copy.

A shallow copy creates a new object which stores the reference of the original elements.

So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself."""
old = [1,2,3]
new = copy.copy(old)
old[1] = 4
print(old)
print(new)
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'
new_list[0][0]='BB'
print("Old list:", old_list)
print("New list:", new_list)

"""When you use copy.copy() to create a shallow copy of a list, a new list is created, but the elements within the list (whether they are simple objects or nested lists) are not duplicated. Instead, the new list holds references to the same objects as the original list. This means that changes to mutable objects (like lists) within the original list will be reflected in the shallow copy and vice versa."""

"""In this example, we have an original list old_list that contains nested lists. We create a shallow copy new_list using copy.copy(). The shallow copy references the same nested lists as the original list.

When we modify an element within a nested list of the shallow copy (new_list[0][0]='BB'), it changes the value in the corresponding element of the original list as well. This is because both the original list and the shallow copy share references to the same nested lists.

The key point here is that while the outer list objects are different (old_list and new_list), the inner list objects are the same in both the original list and the shallow copy. This is what is meant by "storing the reference of the original elements." Changes made to the shared elements will be visible in both the original and shallow copy."""

"""Deep Copy

A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
Deep copy creates a new object that contains independent copies of all the objects in the original object. This means that any changes made to the original object will not be reflected in the deep copy."""

"""
    Shallow copy is faster than deep copy.
    Deep copy is more memory-intensive than shallow copy.
    Shallow copy is not recursive, while deep copy is recursive. This means that shallow copy only copies the first level of objects in the original object, while deep copy copies all levels of objects in the original object.
    Some objects, such as custom classes, cannot be shallowly copied. In these cases, you will need to use deep copy.

"""
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)



"""List Comprehension"""

print([i for i in range(10) if i % 2 == 0])

for index,value in enumerate(list1):
    print(f"index:{index},value:{value}")

print(list1)

for item in zip(list1,list1):
    print(item)

for items in zip(*zip([1, 2, 3], [4, 5, 6])):
    print(items)

for items in zip([1, 2, 3, 4], [1, 2]):
    print(items)
motorcycles = ['honda', 'yamaha', 'suzuki']
a,*ans = 1,2,3
print(type(ans))
(a, b), (c, d) = (1, 2), (3, 4)
print(a,b,c,d)
"""You can add a new element at any position in your list by using the insert()
method. You do this by specifying the index of the new element and the
value of the new item."""
motorcycles.insert(0, 'ducati')
print(motorcycles)

"""If you know the position of the item you want to remove from a list, you can
use the del statement."""
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
del languages[0 : 2]  
print(languages)

"""If you only know the value of the item you want to remove, you can use the remove() method."""
motorcycles.remove('ducati')
print(motorcycles)

"""The list pop() method removes the item at the specified index. The method also returns the removed item.if not specify the index it will remove the last item"""
prime_numbers = [2, 3, 5, 7]
removed_element = prime_numbers.pop(2)
print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)




list2 = list1 
"""same copy"""
list2[0] = 1000
print(list1)

list1=[100,200,300,400]
size = len(list1)
for i in range(size-1,-1,-1):
    print(list1[i],end=' ')

print('\n')
print(list1[size-1::-1])
"""start value is inclusive and stop value is exclusive.so printing till first value -(size-1) or give nothing"""
print(list1[size-1:0:-1])
print('mohim')
print(list1[:-1])
print(list1[1:])
a = [1,2,3,4,5,6]
print(a[len(a):-len(a)-1:-1])













