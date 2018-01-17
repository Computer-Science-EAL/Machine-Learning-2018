#
# Hello, world!
print('Hello, world!')

#
# Array/List
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
b_list = ['a', 'b', 'c', 'd', 'e']

#
# Dictionary
a_dict = {1: 'a', 2: 'b', 3: 'c'}
b_dict = {'a': 1, 'b': 2, 'c': 3}

#
# Loops
x = 0
while x < 10:
    print(x)

for i in range(0, 10):
    print(i)

[print(a) for a in range(0, 10)]

for key, value in a_dict.items(): print('key is {}, value is: {}'.format(key, value))

#
# Statements
the_meaning_with_life = 42
if the_meaning_with_life is 10:
    print('I do not read books...')
elif the_meaning_with_life is not True and 1 == 1 or 1 < False:
    print('I have no idea what just happened')
elif the_meaning_with_life is 42:
    print('Then what is the question?')
else:
    print('I will never travel through the galaxy...')


#
# Functions
def the_function(value1, value2):
    do_something = value1 + value2
    return do_something


#
# Operators
3 + 3  # Addition
3 - 3  # Subtraction
3 * 3  # Multiplication
3 / 3  # Division
3 ** 3  # Exponent
9 // 2  # Floor Division

#
# Lambda
my_lambda = lambda x: x ** x + 2
my_lambda(8)


#
# Class
class my_class(object):
    def __init__(self):
        self.x = 1

    def __str__(self):
        return str(self.x)

my_object = my_class()