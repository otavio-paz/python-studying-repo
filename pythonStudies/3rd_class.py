a = int(input('Type the first grade: '))  # technically, the user could type the wrong grade again.
if a > 10:
    a = int(input("Invalid grade. First grade: "))

b = int(input('Type the second grade: '))
if b > 10:
    b = int(input('Invalid grade. Second grade: '))

c = int(input('Type the third grade: '))
if c > 10:
    c = int(input('Invalid grade. Third grade: '))

d = int(input('Type the fourth grade: '))
if d > 10:
    d = int(input('Invalid grade. Fourth grade: '))

media = (a + b + c + d)/2

if a > 10 and b > 10 and c > 10 and d > 10:
    print('Average: {}'.format(media))
else:
    print('A invalid grade was typed')

# a = int(input('First number: '))
# b = int(input('Second number: '))
# c = int(input('Third number: '))
#
# if a > b and a > c:
#     print('The greater number is {}.'.format(a))
# elif b > a and b > c:
#     print('The greater number is {}.'.format(b))
# else:
#     print('The greater number is {}.'.format(c))
# print('End of the program.')
