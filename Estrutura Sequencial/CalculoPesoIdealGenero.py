genero = int(input(
    'Selecione seu gênero abaixo. \n'
    '[1] Para Masculino \n'
    '[2] Para Feminino \n'
    'Resposta: '
))
altura = float(input('\nInforme sua altura: '))

if genero == 1:
    peso_ideal = (72.7 * altura) - 58
elif genero == 2:
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0

print(f'\nO seu peso ideal é: {peso_ideal:.2f}')
input('\nTecle "ENTER" para sair...')
