a1 = 8
a2 = 5
a3 = 10

for i in range(1,4):
    for j in range(2,5):
        a3 = a3 + 2*a2 - a1
    a1 = a1 - 1
print(a3)