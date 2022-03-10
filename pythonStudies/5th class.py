numbers_list = [1, 3, 5, 7]
animals_list = ['dog', 'cat', 'elephant']

print(numbers_list)  # it will print [1, 3, 5, 7]

print(animals_list[1])  # print cat

for x in animals_list:
    print(x)

# a harder way
n_sum = 0
for y in numbers_list:
    n_sum += y
print(n_sum)

# you can do this
print(sum(numbers_list))  # it will print the sum of the numbers

print(max(numbers_list))  # it will print the maximum number

print(min(numbers_list))  # it will print the minimum number

# it works with words as well

print(max(animals_list))  # as elephant start with an 'e', it's greater than
# 'c' as in cat and 'd' as in dog
print(min(animals_list))  # cat

if 'cat' in animals_list:
    print("There's a cat in the list")
else:
    print("There's not cat in the list")

# you can multiply a list

new_list = animals_list * 3
print(new_list)

animals_list.append('wolf')  # it will add 'wolf' in the list

animals_list.pop()  # it will remove the last thing in the list
animals_list.pop(0)  # it will remove the thing 0 index

animals_list.remove('elephant')  # it will remove elephant

# you can order a list

numbers_list_2 = [12, 10, 7, 5]
print(numbers_list_2)
numbers_list_2.sort()  # it will arrange the list, ascending order
print(numbers_list_2)

numbers_list_2.reverse()  # it will reverse the list

# TUPLES - can't change it

tuple1 = (1, 2, 3, 5, 10)  # we use parentheses for tuples
print(tuple1[1])

# tuple1[0] = 12 error message

print(len(tuple1))  # it will count how many itens are there
print(len(numbers_list_2))

animals_tuple = tuple(animals_list)  # it will convert from the list to tuple

numbers_list_3 = list(tuple1)