import math

print("|=====================|\n"
      "|   EQUAÇÃO 2° GRAU   |\n"
      "|=====================|")

A = int(input("Informe o valor de A: "))

if A == 0:
    print("A equação não é de segunda grau!")
else:
    B = int(input("Informe o valor de B: "))
    C = int(input("Informe o valor de C: "))
    delta = B*B-(4*A*C)

    if delta < 0:
        print("A equação não possui raizes reais!")
    elif delta == 0:
        raiz = -B/(2*A)
        print(f"O delta é igual a 0 e sua raiz é: {raiz}")
    else:
        raiz1 = (-B + math.sqrt(delta)) / (2*A)
        raiz2 = (-B - math.sqrt(delta)) / (2*A)
        print(f"O delta é positivo!"
              f"\nPrimeira raiz: {raiz1:.2f}"
              f"\nSegunda raiz: {raiz2:.2f}")
