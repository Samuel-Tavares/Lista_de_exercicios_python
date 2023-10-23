numero = int(input('Informe um número menor do que 1000: '))

if numero >= 1 and numero < 1000:
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10
else:
    print('Valor inválido. Tente novamente!')

print(f'Valor forncecido: {numero}\n'
      f'O mesmo tem: \n'
      f'{centena} centena(s)\n'
      f'{dezena} dezenas(s)\n'
      f'{unidade} unidade(s)\n'
      )
