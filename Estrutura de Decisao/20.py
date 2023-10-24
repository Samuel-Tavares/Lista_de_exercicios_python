quantidade_de_notas = int(input('Quantas notas serão calculadas: '))
notas = []


def calculo_media(nota, qtd_de_notas):
    media = sum(nota) / qtd_de_notas

    return media


def verificando_media(media):
    if media < 7:
        return False
    else:
        return True


for i in range(1, quantidade_de_notas + 1):
    nota = float(input(f'Informe a {i}° nota:'))
    notas.append(nota)

media = calculo_media(notas, quantidade_de_notas)
aproveitamento = verificando_media(media)

if media == 10:
    print(f'\nResultado: Aprovado com distinção!\nMédia: {media:.1f}')
elif aproveitamento:
    print(f'\nResultado: Aprovado!\nMédia: {media:.1f}')
else:
    print(f'\nResultado: Reprovado\nMédia: {media:.1f}')
