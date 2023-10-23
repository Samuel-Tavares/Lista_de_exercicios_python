def decrescente():
    if numero1 > numero2 and numero2 > numero3:
        print(f"{numero1}\n{numero2}\n{numero3}")

    elif numero3 > numero2 and numero2 > numero1:
        print(f"{numero3}\n{numero2}\n{numero1}")

    elif numero2 > numero1 and numero1 > numero3:
        print(f"{numero2}\n{numero1}\n{numero3}")

    elif numero2 > numero1 and numero3 > numero1:
        print(f"{numero2}\n{numero3}\n{numero1}")

    elif numero3 > numero1 and numero1 > numero2:
        print(f"{numero3}\n{numero1}\n{numero2}")
    else:
        print(f"{numero1}\n{numero3}\n{numero2}")


numero1 = int(input('Informe o 1° numero: '))
numero2 = int(input('Informe o 2° numero: '))
numero3 = int(input('Informe o 3° numero: '))

print('-'*40)

decrescente()
