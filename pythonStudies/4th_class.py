a = int(input('Type the first grade: '))  # technically, the user could type the wrong grade again.
while a > 10:
    a = int(input("Invalid grade. First grade: "))

b = int(input('Type the second grade: '))
while b > 10:
    b = int(input('Invalid grade. Second grade: '))

c = int(input('Type the third grade: '))
while c > 10:
    c = int(input('Invalid grade. Third grade: '))

d = int(input('Type the fourth grade: '))
while d > 10:
    d = int(input('Invalid grade. Fourth grade: '))

media = (a + b + c + d)/2

if a > 10 and b > 10 and c > 10 and d > 10:
    print('Average: {}'.format(media))
else:
    print('A invalid grade was typed')







a = 0
while a < 10:
    print(a)  # from 0 to 9
    a += 1  # a = a + 1

for i in range(101):
    div = 0
    for x in range(1, i + 1):
        modulus = i % x
        if modulus == 0:
            div += 1  # div = div + 1
    if div == 2:
        print(i)  # print all the prime numbers

# range goes from 0 to 99
for x in range(100):  # range (1, 100) but not 1 nor 100 included
    print(x)

div = 0

a = int(input('Type a number: '))

# check if the number 'a' is divisible by 'x', then see if it's prime
for x in range(1, a + 1):
    modulus = a % x
    print(x, modulus)
    if modulus == 0:
        div += 1  # div = div + 1
if div == 2:
    print('The number {} is prime.'.format(a))
else:
    print('The number {} is not prime.'.format(a))
