# Já que não há switch case, dá para usar uma biblioteca

import calendar

while True:
    mes = int(input('Digite um número de 1 a 12 para um mês: '))
    if mes > 0 and mes < 12:
        print(calendar.month_name[mes])
        break
    else:
        print('Número inválido!')
