import math

metros_quadrados_por_litro = 6
litros_lata = 18
litros_galao = 3.6
preco_lata = 80
preco_galao = 25
acrescimo = 1.1

area = float(input('Informe a área em m² a ser pintada: '))
litros_necessarios = (area / metros_quadrados_por_litro) * acrescimo

latas_necessarias = math.ceil(litros_necessarios / litros_lata)
valor_latas = latas_necessarias * preco_lata

galoes_necessarios = math.ceil(litros_necessarios / litros_galao)
valor_galoes = galoes_necessarios * preco_galao

lata_para_misturar = math.floor(litros_necessarios / litros_lata)
diferenca_para_misturar = litros_necessarios % litros_lata
galao_para_misturar = math.ceil(diferenca_para_misturar / litros_galao)
preco_lata_para_misturar = lata_para_misturar * preco_lata
preco_galao_para_misturar = galao_para_misturar * preco_galao
valor_misturado = preco_lata_para_misturar + preco_galao_para_misturar

print(f'\nPara pintar uma área de {area}m² você precisará de '
      f'{litros_necessarios:.2f} litros.\nTemos as seguintes opções:'
      f'\nComprando apenas latas de {litros_lata}L: {latas_necessarias}'
      f' latas.'
      f'\nValor Total: R${valor_latas:.2f}\n'
      f'\nComprando apenas galões de {litros_galao}L: {galoes_necessarios}'
      f' galão(ões).'
      f'\nValor Total: R${valor_galoes:.2f}\n'
      f'\nPara economizar você pode comprar {lata_para_misturar} lata(s)'
      f' e {galao_para_misturar} galão(ões).'
      f'\nValor Total: R${valor_misturado:.2f}'
      )
