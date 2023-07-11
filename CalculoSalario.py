valor_hora = float(input('Informe o valor da sua hora: '))
horas_trabalhadas = float(input('Horas trabalhadas no mês: '))

salario = horas_trabalhadas * valor_hora

print(
    f'\nSeu salário de acordo com as horas trabalhadas foi: R${salario:.2f}')

input('\nTecle "ENTER" para sair...')
