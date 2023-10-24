def calculo_valor_compra(kg_morango, kg_maca):
    kg_totais = kg_maca + kg_morango

    if kg_morango <= 5:
        preco_kg_morango = 2.50
    else:
        preco_kg_morango = 2.20

    if kg_maca <= 5:
        preco_kg_maca = 1.80
    else:
        preco_kg_maca = 1.50

    v_compra = (kg_morango * preco_kg_morango) + (
        kg_maca * preco_kg_maca)

    if kg_totais > 8 or v_compra > 25:
        desconto_aplicado = v_compra * 0.10
        v_compra = v_compra - desconto_aplicado

    return v_compra


qtd_kg_morango = int(input("Quantidade Kg de morango: "))
qtd_kg_maca = int(input("Quantidade Kg de maças: "))

valor_compra = calculo_valor_compra(qtd_kg_morango, qtd_kg_maca)

print(f"Valor total da compra: {valor_compra}")
