letters_counter = lambda list: [len(x) for x in list]

animals_list = ['dog', 'cat', 'elephant']
print(letters_counter(animals_list))

n_sum = lambda a, b: a + b
sub = lambda a, b: a - b

print(n_sum(5, 10))
print(sub(10, 2))

calculator ={   # criar dicionario
    'Sum':lambda a, b: a + b,
    'Subtraction': lambda a, b: a - b,
    'Multiplication': lambda a, b: a * b,
    'Division': lambda a, b: a / b,
}

soma = calculator['Sum']  # it's basically doing soma = lambda a, b: a + b,
multipl = calculator['Multiplication']
print(soma(10, 5))