primeiro_inteiro = int(input('Informe um número inteiro: '))
segundo_inteiro = int(input('Informe um segundo número inteiro: '))
numero_real = float(input('Agora informe um número real: '))

produto = 2 * primeiro_inteiro * (segundo_inteiro / 2)
soma = (3 * primeiro_inteiro) + numero_real
terceiro_valor_elevado_ao_cubo = numero_real ** 3

print('\n| CALCULOS |\n')
print('Cálculo do produto do dobro do primeiro número com metade do segundo.\n'
      'Resultado: ' + str(produto) + '\n'
      )

print(
    'Soma do triplo do primeiro com o terceiro(real).\n'
    'Resultado: ' + str(soma) + '\n'
)

print('Terceiro valor(real) elevado ao cubo.\n'
      f'Resultado: {terceiro_valor_elevado_ao_cubo:.2f}'
      )

input('\nTecle "ENTER" para sair...')
