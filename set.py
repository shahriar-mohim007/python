"""Set is an unordered collection of unique elements. This means that when you add elements to a set, they are not stored in any specific order, and when you iterate over the elements of a set, there is no guaranteed sequence in which the elements will be returned"""

student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)
empty_set = set()

numbers = {21, 34, 54, 12}

print('Initial Set:',numbers)
numbers.add(32)

print('Updated Set:', numbers) 


companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)

print(companies)

languages = {'Swift', 'Java', 'Python'}

print('Initial Set:',languages)

removedValue = languages.discard('Java')

print('Set after remove():', languages)


