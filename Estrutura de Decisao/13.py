def dia_da_semana():
    if 1 <= numero <= 7:
        if numero == 1:
            print(f'{numero} - Domingo')
        elif numero == 2:
            print(f'{numero} - Segunda')
        elif numero == 3:
            print(f'{numero} - Terça Feira')
        elif numero == 4:
            print(f'{numero} - Quarta Feira')
        elif numero == 5:
            print(f'{numero} - Quinta Feira')
        elif numero == 6:
            print(f'{numero} - Sexta Feira')
        else:
            print(f'{numero} - Sábado')
    else:
        print(f'{numero} - Número inválido!')


numero = int(input('Informe um número e mostrarei a qual dia '
                   'da semana pertence: '))

dia_da_semana()
