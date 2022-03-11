from datetime import date, time, datetime, timedelta

def trabalhando_com_timedelta():
    data_string = '01/01/2019 12:20:22'  # converter de string para datetime
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)  #01/01/2018


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)  # não será string
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.day)
    print(data_atual.year)
    print(data_atual.weekday())

    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])

    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

    data_string = '01/01/2019'  #converter de string para datetime
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)


def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%y')  # deixar dia/mes/ano
    # porém, ela não é string
    print(data_atual_str)


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)  # vai printar 15:18:30 mas não é string
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)  # será string


if __name__ == '__main__':
    trabalhando_com_date()
