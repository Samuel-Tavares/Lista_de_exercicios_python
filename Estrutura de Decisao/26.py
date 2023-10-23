def verificando_opcao(op):
    if op == "a":
        return True
    elif op == "g":
        return True
    else:
        return False


def calculo_valor(op, litro_v):
    valor_litro_alcool = 1.90
    valor_litro_gasolina = 2.50

    if op == "a":
        if litro_v <= 20:
            desconto_aplicado = valor_litro_alcool * 0.03
            valor_p_l = valor_litro_alcool - desconto_aplicado
        else:
            desconto_aplicado = valor_litro_alcool * 0.05
            valor_p_l = valor_litro_alcool - desconto_aplicado
    elif opcao == "g":
        if litro_v <= 20:
            desconto_aplicado = valor_litro_gasolina * 0.04
            valor_p_l = valor_litro_gasolina - desconto_aplicado
        else:
            desconto_aplicado = valor_litro_gasolina * 0.06
            valor_p_l = valor_litro_gasolina - desconto_aplicado

    valor_v = litro_v * valor_p_l

    return valor_p_l, valor_v


litros_vendidos = int(input("Litros vendidos: "))

opcao = input("\n[SELECIONE O COMBUSTÍVEL]\n"
              "[OPÇÃO:                 ]\n"
              "[A -> ÁLCOOL            ]\n"
              "[G -> GASOLINA          ]\n"
              "\nR:").lower()

if verificando_opcao(opcao):
    valor_por_litro, valor_venda = calculo_valor(opcao, litros_vendidos)
    print(f"\nValor a pagar: R${valor_venda:.2f}")
else:
    print("Opção inválida!")
