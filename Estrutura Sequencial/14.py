peso_limite = 50

print('\n| CÁLCULO PESO DOS PEIXES |\n')
peso_peixe = float(input('Informe o peso do(s) peixe(s): '))

excesso = peso_peixe - peso_limite

if excesso > 0:
    multa = excesso * 4
    print(
        '\nVocê excedeu ' + str(excesso) +
        'Kg do peso limite de ' + str(peso_limite) + 'Kg estabelecido.'
    )
    print('\nO valor da multa a ser paga é de: ' + str(multa))
else:
    excesso < 0
    multa = 0
    print('\nVocê não excedeu o peso de ' + str(peso_limite)
          + 'Kg estabelecido.'
          '\nTotal de multa a pagar: ' + str(multa)
          )

input('\nTecle "ENTER" para sair...')
