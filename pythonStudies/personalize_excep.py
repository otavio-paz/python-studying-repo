class Error(Exception):  # classe herda de Exception
        pass             # precisa de uma classe sem nada e outra personalizada

class InputError(Error):  # recomenda-se sempre terminar com error em classes de erros
    def __init__(self, message):   # construtor
        self.message = message

while True:
    try:
        x = int(input('Entre com um número de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')  # raise força o lançamento de exception
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
            print(ex)