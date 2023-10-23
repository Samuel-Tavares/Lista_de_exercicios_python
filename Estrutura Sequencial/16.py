area = float(input('Informe a área em M² a ser pintada: '))

litros_por_lata = 18
valor_lata_de_tinta = 80
quantidade_de_latas_para_comprar = (area / 3) / litros_por_lata
valor_da_compra = quantidade_de_latas_para_comprar * valor_lata_de_tinta

print('\n| RESUMO |'
      '\nquantidade de latas a comprar: ' +
      str(round(quantidade_de_latas_para_comprar)) + ' latas.'
      f'\nValor total: R${valor_da_compra:.2f}'
      )
