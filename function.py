def addition(*args):
    result = 0
    for value in args:
        result += value
    return result

print(addition(2, 29, 150, 46))

def example_function_for_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


example_function_for_args_kwargs('first_value', 'second_value', 2, 3, 4, 4.5, name='Noyon', company='Craftsmen', bla='bla')

"""In Python, a lambda function is a special type of function without the function name."""

# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)
greet_user('Delilah')


multi = lambda num, num2: num * num2
print(multi(7, 5))


"""The filter() function in Python takes in a function and an iterable (lists, tuples, and strings) as arguments.

The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True."""

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

"""The map() function in Python takes in a function and an iterable (lists, tuples, and strings) as arguments.

The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item."""



"""The filter() function selects elements from an iterable (list, tuple etc.) based on the output of a function.

The function is applied to each element of the iterable and if it returns True, the element is selected by the filter() function."""


# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)

new_list = list(map(int,input().split()))

print((lambda x, y: x + y)(1, 2))