valor_hora = float(input('Informe o valor da sua hora: '))
horas_trabalhadas = float(input('Horas trabalhadas no mês: '))

salario_bruto = horas_trabalhadas * valor_hora
ir = (11/100) * salario_bruto
inss = (8/100) * salario_bruto
sindicato = (5/100) * salario_bruto
salario_liquido = salario_bruto - ir - inss - sindicato

print('\n|    DESCRIÇÃO DE PAGAMENTO    |')
print(f'|+ Salário Bruto   : R${salario_bruto:.2f} |'
      f'\n|- IR (11%)        : R${ir:.2f}  |'
      f'\n|- INSS (8%)       : R${inss:.2f}  |'
      f'\n|- Sindicato (5%)  : R${sindicato:.2f}   |'
      f'\n|= Salário Líquido : R${salario_liquido:.2f} |'
      )

input('\nTecle "ENTER" para sair...')
