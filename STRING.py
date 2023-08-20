"""Python Strings are immutable"""
"""Immutable objects are passed by value"""
"""
Immutable objects
Numbers
Strings
Tuples
Frozen Sets
"""

import string 
import datetime
def test_func1(s):
    print(id(s))
    size = len(s)
    for i in range(size):
        if s[i]=='M':
           s = s[:i] +'W'+s[i+1:]
    
    return s
"""replace() Arguments

The replace() method can take a maximum of three arguments:

    old - the old substring we want to replace
    new - new substring which will replace the old substring
    count (optional) - the number of times you want to replace the old substring with the new string
"""
def test_func2(s):
    size = len(s)
    for i in range(size):
        if s[i]=='M':
           s = s.replace(s[i],'W')
        elif s[i] =='O':
           s = s.replace(s[i],'A')
    
    return s


def test_func3(s):
    byte_array = bytearray(s, 'utf-8')  
    size = len(byte_array)
    
    for i in range(size):
        if byte_array[i] == ord('M'):  
            byte_array[i] = ord('W')
        elif byte_array[i] == ord('O'):
            byte_array[i] = ord('A')
    
    return byte_array.decode('utf-8')

def test_func4(s):
    s= "-".join(s)
    return s

def test_func5(s):
    s= s.split('-') 
    """Converted in list"""
    s=''.join(s)
    return s
s="MOHIM"
print(id(s))
a=test_func1(s)
print(id(a))
print(test_func1(s))
print(test_func2(s))
print(test_func3('MOHIM'))
print(test_func4('MOHIM'))
print(test_func5('M-O-H-I-M'))
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('{a}, {b}, {c}'.format(a='a', b='b', c='c'))
print("The number is:{:d}".format(123))
print("The float number is:{:.1f}".format(123.4567898))
print("{:5d}".format(12))
print("{:8.3f}".format(12.2346))
print("{:08.3f}".format(12.2346))
print("{:=8.3f}".format(-12.2346))
print("{:.3}".format("caterpillar"))
print("{:5.3}".format("caterpillar"))
print("{:^5.3}".format("caterpillar"))
print("{:>5}".format("cat"))
date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))

person = {'age': 23, 'name': 'Adam'}
print("{p[name]}'s age is: {p[age]}".format(p=person))
print("{name}'s age is: {age}".format(**person))

class Person:
    age = 23
    name = "Adam"
print("{p.name}'s age is: {p.age}".format(p=Person()))
s="BANGLADESH"
s = s[len(s)-1:-len(s)-1:-1]
"""start value is inclusive and stop value is exclusive
start:stop:step"""
print(s)
s = s[0:len(s):2]
print(s)

pi = 3.141592653589793
formatted_pi = f"Value of pi: {pi:.2f}"
print(formatted_pi) 


number = 123.4567898
formatted_string = f"The float number is: {number:.1f}"
print(formatted_string) 
print(f"{'mohimmmmmmmmm':.5}")

s = '  MOHIM  '

print(s.strip())


import copy
s1 = 'mohim'
print(id(s1))
s = copy.copy(s1)
print(id(s))
s1=s1.upper()
print(s,s1)
print(id(s1))
size = len(s)
for i in range(size):
    if s[i]=='M':
        s = s.replace(s[i],'W')
    elif s[i] =='O':
        s = s.replace(s[i],'A')

print(id(s))

"""A shallow copy of a string is essentially a reference to the same string object. Since strings are immutable, any modifications to one copy will not affect the other. However, both copies will still refer to the same underlying string data in memory."""