numeros = []

for i in range(2):
    numero = float(input('Digite um número: '))
    numeros.append(numero)

    maior_numero = max(numeros)

print(f'Os números digitados foram: {numeros}')
print('O maior número digitado foi: ', maior_numero)
