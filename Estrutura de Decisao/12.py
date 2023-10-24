salario_liquido, deposito_fgts, desconto_inss, desconto_sindicato = 0, 0, 0, 0
desconto_ir, total_descontos, percentual_ir = 0, 0, 0


def descontos(salario_bruto):

    deposito_fgts = ((11/100) * salario_bruto)
    desconto_inss = ((10/100) * salario_bruto)
    desconto_sindicato = ((3/100) * salario_bruto)

    if salario_bruto <= 900:
        desconto_ir = 0
        percentual_ir = (0/100) * 100
        salario_liquido = (salario_bruto - desconto_ir - desconto_inss
                           - desconto_sindicato)

    elif 901 <= salario_bruto <= 1500:
        desconto_ir = ((5/100) * salario_bruto)
        percentual_ir = (5/100) * 100
        salario_liquido = (salario_bruto - desconto_ir - desconto_inss
                           - desconto_sindicato)

    elif 1500 <= salario_bruto <= 2500:
        desconto_ir = ((10/100) * salario_bruto)
        percentual_ir = (10/100) * 100
        salario_liquido = (salario_bruto - desconto_ir - desconto_inss
                           - desconto_sindicato)

    else:
        desconto_ir = ((20/100) * salario_bruto)
        percentual_ir = (20/100) * 100
        salario_liquido = (salario_bruto - desconto_ir - desconto_inss
                           - desconto_sindicato)

    total_descontos = (salario_bruto - desconto_ir - desconto_inss -
                       desconto_sindicato)

    return (salario_liquido, deposito_fgts, desconto_inss, desconto_sindicato,
            desconto_ir, total_descontos, percentual_ir)


valor_hora = float(input('Valor da hora: '))
horas_trabalhadas = float(input('Horas trabalhadas: '))

salario_bruto = valor_hora * horas_trabalhadas

(salario_liquido, deposito_fgts, desconto_inss, desconto_sindicato,
 desconto_ir, total_descontos, percentual_ir) = descontos(salario_bruto)

print(f'Salário Bruto          : R${salario_bruto:.2f}\n'
      f'(-) IR ({percentual_ir:.0f})%           : R${desconto_ir:.2f}\n'
      f'(-) INSS (10%)         : R${desconto_inss:.2f}\n'
      f'FGTS (11%)             : R${deposito_fgts:.2f}\n'
      f'Salário Líquido        : R${salario_liquido:.2f}\n'
      )
