set1 = {1, 2, 3, 4}

set1.add(5)  # ad the 5 element
set1.discard(2)  # remove 2 element
print(type(set1))  # <class 'set'

set2 = {1, 2, 3, 4, 5}
set3 = {5, 6, 7, 8}

union_set = set2.union(set3)
print('Union:  {}'.format(union_set))

intersec_set = set2.intersection(set3)
print('Intersection: {}'.format(intersec_set))

diff_set = set2.difference(set3)
print('Difference: {}'.format(diff_set))

sim_diff_set = set2.symmetric_difference(set3)
print('Symmetric difference: {}'.format(sim_diff_set))  # it will return the combination of things that makes the
# sets different to each other

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

subset = set_a.issubset(set_b)
print(subset)  # true, it's a subset

superset = set_b.issuperset(set_a)
print(superset)  # true, it's a superset

animals_list = ['dog', 'dog', 'cat', 'cat', 'elephant']
animals_set = set(animals_list)
