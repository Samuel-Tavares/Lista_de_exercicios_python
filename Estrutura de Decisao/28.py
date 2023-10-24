import sys


def precificando_carne(escolha_carne):
    if carne_escolhida == 1:
        if kg_carne <= 5:
            valor_carne = 4.90
        else:
            valor_carne = 5.80
    elif carne_escolhida == 2:
        if kg_carne <= 5:
            valor_carne = 5.90
        else:
            valor_carne = 6.80
    elif carne_escolhida == 3:
        if kg_carne <= 5:
            valor_carne = 6.90
        else:
            valor_carne = 7.80
    else:
        sys.exit("Ops!!! Algo deu errado, procure um responsável!")

    return valor_carne


def verificando_tipo_carne(escolha_carne):
    if escolha_carne == 1:
        TipoDeCarne = "Filé Duplo"
    elif escolha_carne == 2:
        TipoDeCarne = "Alcatra"
    else:
        TipoDeCarne = "Picanha"

    return TipoDeCarne


def tipo_pagamento(forma_pag):
    if forma_pag == 1:
        tipo_pag = "Crédito Tabajara"
    elif forma_pag == 2:
        tipo_pag = "Débito"
    elif forma_pag == 3:
        tipo_pag = "Crédito"
    else:
        tipo_pag = "Dinheiro"

    return tipo_pag


carne_escolhida = int(input("|=======================|\n"
                            "| HIPERMERCADO TABAJARA |\n"
                            "|=======================|\n"
                            "|         CARNES        |\n"
                            "| 1 - File Duplo        |\n"
                            "| 2 - Alcatra           |\n"
                            "| 3 - Picanha           |\n"
                            "|=======================|\n"
                            "|OPÇÃO: "
                            ))

TipoDeCarne = verificando_tipo_carne(carne_escolhida)

kg_carne = int(input("Kg de carne adquirida: "))

valor_carne = precificando_carne(carne_escolhida)

forma_pagamento = int(input("\n|=====================|\n"
                            "|  FORMA DE PAGAMENTO |\n"
                            "|=====================|\n"
                            "| 1 - Crédito Tabajara|\n"
                            "| 2 - Débito          |\n"
                            "| 3 - Crédito         |\n"
                            "| 4 - Dinheiro        |\n"
                            "|OPÇÃO: "
                            ))

if forma_pagamento < 1 or forma_pagamento > 4:
    sys.exit("Ops!!! Algo deu errado, procure um responsável!")

TipoPagamento = tipo_pagamento(forma_pagamento)

preco_total = valor_carne * kg_carne

if forma_pagamento == 1:
    desconto_aplicado = preco_total * 0.05
    valor_a_pagar = preco_total - desconto_aplicado

print(f"\n|=======================|\n"
      f"|     CUPOM FISCAL      |\n"
      f"|=======================|\n"
      f"|TIPO DE CARNE: {TipoDeCarne}\n"
      f"|QUANTIDADE EM KG: {kg_carne}\n"
      f"|PREÇO TOTAL: R${preco_total:.2f}\n"
      f"|TIPO DE PAGAMENTO: {TipoPagamento}\n"
      f"|VALOR DO DESCONTO: R${desconto_aplicado:.2f}\n"
      f"|VALOR A PAGAR: R${valor_a_pagar}\n"
      )
