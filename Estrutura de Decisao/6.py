maior_numero = 0

for i in range(1, 4):
    numero = int(input(f'Informe o {i}° número: '))

    if numero > maior_numero:
        maior_numero = numero

print(f'O maior número digitado foi: {maior_numero}')
