lista = [1, 10]
arquivo = open('teste.txt', 'r')

try:
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[1]
    print('fechando arquivo') # nao irá mostrar, pois tem um erro anterior
except ZeroDivisionError:  # do mais especifico pra o geral - verificar hierarquia
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex:  # toda outra exceção, vai cair aqui
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('fechando arquivo')
    arquivo.close()