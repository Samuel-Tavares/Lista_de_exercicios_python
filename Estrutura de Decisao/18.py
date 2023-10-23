def verificando_data(data):
    try:
        dia, mes, ano = map(int, data.split('/'))

        if ano < 1 or ano > 9999:
            return False

        if mes < 1 or mes > 12:
            return False

        dias_no_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            dias_no_mes[2] = 29

        if dia < 1 or dia > dias_no_mes[mes]:
            return False

        return True

    except ValueError:
        return False


data = input('Informe uma data no formato dd/mm/aaaa: ')

if verificando_data(data):
    print('A data é válida!')
else:
    print('A data não é válida!')
