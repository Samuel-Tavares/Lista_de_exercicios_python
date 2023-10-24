def conferindo_positivas(p1, p2, p3, p4, p5):
    qtd_positivas = 0

    if p1 == "sim":
        qtd_positivas += 1

    if p2 == "sim":
        qtd_positivas += 1

    if p3 == "sim":
        qtd_positivas += 1

    if p4 == "sim":
        qtd_positivas += 1

    if p5 == "sim":
        qtd_positivas += 1

    return qtd_positivas


def classificando_positivas(qtd_positivas):
    if qtd_positivas == 2:
        classificacao = "Suspeito"
    elif qtd_positivas == 3 or qtd_positivas == 4:
        classificacao = "Cúmplice"
    elif qtd_positivas == 5:
        classificacao = "Assassino"
    else:
        classificacao = "Inocente"

    return classificacao


print('\nResponda com "sim" ou "não"!\n')
pergunta_1 = input("Telefonou para a vítima? R:").lower()
pergunta_2 = input("Esteve no local do crime? R:").lower()
pergunta_3 = input("Mora perto da vítima? R:").lower()
pergunta_4 = input("Devia para a vítima? R:").lower()
pergunta_5 = input("Trabalhou com a vítima? R:").lower()

quantidade_positivas = (conferindo_positivas(pergunta_1, pergunta_2,
                                             pergunta_3, pergunta_4,
                                             pergunta_5))

classificacao = classificando_positivas(quantidade_positivas)


print(f"\nQuantidade positivas: {quantidade_positivas}\n"
      f"Classificação: {classificacao}\n")
