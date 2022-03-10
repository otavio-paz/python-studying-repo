a = int(input('Type a first number: '))
b = int(input('Type a second number: '))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
print(type(addition))  # returns the value of the variable

print('Addition: ' + str(addition))
print('Subtraction: ' + str(subtraction))
print('Multiplication: ' + str(multiplication))
print('Division: ' + str(division))
print('Modulus: ' + str(modulus))

# division is a float type, if I want to round it up, I just need to convert to int, e.g.
print(int(division))

# also, from string to int, like:
x = '1'
print(int(x))

# CTRL \ to comment more than one line

# another way to print a string and a variable's value is to use .format

print('Addition: {}'.format(addition))

print('Subtraction: {} - Multiplication: {}'.format(subtraction, multiplication))

# one more way to do that

print('Division: {div} \n Modulus: {mod}'.format(div=division,
                                                mod=modulus))

