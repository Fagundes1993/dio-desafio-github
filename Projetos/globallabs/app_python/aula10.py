from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime(' %A %D ')
    print(data_atual)

def trabalhando_com_time():
    horario = time(hour=15, minute= 18, second=30)
    horario_str = horario.strftime('%H %M %S')
    print(horario)

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%c'))
    nova_data = data_atual - timedelta(days=365)
    print(nova_data)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()