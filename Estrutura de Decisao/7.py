menor_numero = 0

for i in range(1, 4):
    numero = int(input(f'Informe o {i}° número: '))

    if numero == 0:
        numero = menor_numero

    if menor_numero == 0 or numero < menor_numero:
        menor_numero = numero

print(menor_numero)
