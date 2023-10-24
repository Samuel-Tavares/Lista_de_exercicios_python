percentual_aplicado = 0
valor_aumento = 0
novo_salario = 0


def reajuste_salario(salario):
    criterio1 = 280
    criterio2 = 700
    criterio3 = 1500
    percentual1 = (20/100)
    percentual2 = (15/100)
    percentual3 = (10/100)
    percentual4 = (5/100)

    if salario <= criterio1:
        novo_salario = salario + percentual1 * salario
        p_aplicado = percentual1 * 100
    elif criterio1 <= salario <= criterio2:
        novo_salario = salario + percentual2 * salario
        p_aplicado = percentual2 * 100
    elif criterio2 <= salario <= criterio3:
        novo_salario = salario + percentual3 * salario
        p_aplicado = percentual3 * 100
    else:
        novo_salario = salario + percentual4 * salario
        p_aplicado = percentual4 * 100

    valor_aumento = novo_salario - salario

    return novo_salario, p_aplicado, valor_aumento


print('| ORGANIZAÇÕES TABAJARA |\n')
salario = float(input('Informe o salário para reajuste: '))
print('-'*40)

novo_salario, percentual_aplicado, valor_aumento = reajuste_salario(salario)

print(f'| INFORMAÇÕES DE REAJUSTE |\n'
      f'\nSalário anterior: R${salario:.2f}\n'
      f'Percentual de aumento: {percentual_aplicado:.0f}%\n'
      f'Valor do aumento: R${valor_aumento:.2f}\n'
      f'Salário reajustado: R${novo_salario:.2f}'
      )
