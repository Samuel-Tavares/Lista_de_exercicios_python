def calculo_bisexto(a):
    if (a % 4 == 0 and a % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False


ano = int(input('Informe um ano: '))

resultado = calculo_bisexto(ano)

print(f'O ano {ano} é bissexto?\nResultado: {resultado}')
