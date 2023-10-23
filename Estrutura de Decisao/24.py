def escolhendo_operacao(escolha, valor1, valor2):
    try:
        if escolha == 1:
            resultado = valor1 + valor2
        elif escolha == 2:
            resultado = valor1 - valor2
        elif escolha == 3:
            resultado = valor1 / valor2
        elif escolha == 4:
            resultado = valor1 * valor2

    except ValueError:
        print("Opção inválida!")

    return resultado


def verificando_resultado(resultado):
    if resultado > 0:
        positivo_ou_negativo = "Positivo"
    else:
        positivo_ou_negativo = "Negativo"

    if resultado % 2 == 0:
        par_ou_impar = "Par"
    else:
        par_ou_impar = "Impar"

    if resultado == round(resultado):
        inteiro_ou_decimal = "Inteiro"
    else:
        inteiro_ou_decimal = "Decimal"

    if inteiro_ou_decimal == "Decimal":
        par_ou_impar = "Não classificado devido ser decimal!"

    return positivo_ou_negativo, par_ou_impar, inteiro_ou_decimal


numero1 = float(input("Informe o primeiro valor: "))
numero2 = float(input("Informe o segundo valor: "))

print("\nQual operação deseja realizar?\n"
      "[1] Para Adição\n"
      "[2] Para Subtração\n"
      "[3] Para Divisão\n"
      "[4] Para Multiplicação\n")

opcao = int(input("Opção: "))

resultado = escolhendo_operacao(opcao, numero1, numero2)

positivo_ou_negativo, par_ou_impar, inteiro_ou_decimal = verificando_resultado(
    resultado)

print(f"\nO resultado da operação foi: {resultado}\n"
      f"O resultado é positivo ou negativo? R: {positivo_ou_negativo}\n"
      f"O resultado é par ou impar? R: {par_ou_impar}\n"
      f"O resultado é inteiro ou decimal? R: {inteiro_ou_decimal}\n")
