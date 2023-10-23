def calculo_media(nota1, nota2):
    quantidade_notas = 2
    media = (nota1 + nota2) / quantidade_notas
    return media


nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media_aluno = calculo_media(nota1, nota2)

if media_aluno == 10:
    print(f'Aprovado com distinção! Média: {media_aluno}')
elif media_aluno >= 7:
    print(f'Aprovado! Média: {media_aluno}')
else:
    print(f'Reprovado! Média: {media_aluno}')
