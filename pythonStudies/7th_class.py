class Calculator:
    def __init__(self):  # quando instanciar, vai passar pelo init
        pass  # não pode ficar sozinho, logo precisa do pass

    def sum_(self, num_a, num_b):  # it's a function because it returns a value
        return num_a + num_b

    def subt(self, num_a, num_b):
        return num_a - num_b

    def mult(self, num_a, num_b):
        return num_a * num_b

    def divi(self, num_a, num_b):
        return num_a / num_b


calculator = Calculator()
print(calculator.sum_(10, 2))
print(calculator.subt(5, 3))
print(calculator.mult(6, 11))
print(calculator.divi(84, 2))
