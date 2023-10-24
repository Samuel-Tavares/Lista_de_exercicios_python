def aproveitamento(nota1, nota2):
    media = (nota1 + nota2) / 2

    if 9.0 <= media <= 10.0:
        conceito = 'A'
    elif 7.5 <= media <= 8.9:
        conceito = 'B'
    elif 6.0 <= media <= 7.4:
        conceito = 'C'
    elif 4.0 <= media <= 5.9:
        conceito = 'D'
    else:
        conceito = 'E'

    if conceito == 'D' or conceito == 'E':
        mensagem = 'Reprovado!'
    else:
        mensagem = 'Aprovado!'

    return media, conceito, mensagem


nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media, conceito, mensagem = aproveitamento(nota1, nota2)

print('-' * 40)
print(f'Primeira Nota: {nota1}\n'
      f'Segunda Nota: {nota2}\n'
      f'Média: {media}\n'
      f'Conceito: {conceito}\n'
      f'Status: {mensagem}'
      )
