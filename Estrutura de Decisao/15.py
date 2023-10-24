def calculo_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return 'Os valores podem se tornar um triângulo!'
    else:
        return 'Os valores não podem se tornar um triângulo!'


def verificando_triangulos(a, b, c):
    if a == b == c:
        return 'Equilátero'
    elif a == b or b == c or a == c:
        return 'Isósceles'
    elif a != b and b != c:
        return 'Escaleno'
    else:
        return 'Não é triângulo!'


lado1 = float(input('Informe o 1° lado do triangulo: '))
lado2 = float(input('Informe o 2° lado do triangulo: '))
lado3 = float(input('Informe o 3° lado do triangulo: '))

resultado = calculo_triangulo(lado1, lado2, lado3)
triangulo = verificando_triangulos(lado1, lado2, lado3)


print(f'Resultado: {resultado}\n'
      f'Tipo de triângulo: {triangulo}\n'
      )
