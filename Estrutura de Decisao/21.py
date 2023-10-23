import os

saldo = 1600


def verifica_saldo(saldo, v_saque):
    try:
        if v_saque >= 10 and v_saque <= saldo:
            return True

    except ValueError:
        return False


def calculo_notas_saque(v_saque):

    qtd_notas1 = 0
    qtd_notas5 = 0
    qtd_notas10 = 0
    qtd_notas50 = 0
    qtd_notas100 = 0

    centena = v_saque // 100
    dezena = (v_saque % 100) // 10
    unidade = v_saque % 10

    qtd_notas100 = centena

    if 5 <= dezena <= 10:
        diferenca_dezenas = dezena - 5
        qtd_notas50 = 1
        qtd_notas10 = diferenca_dezenas

    if 1 <= dezena <= 4:
        qtd_notas10 = dezena
    elif dezena == 5:
        qtd_notas50 = 1

    if unidade > 5 and unidade < 10:
        diferenca_unidades = unidade - 5
        qtd_notas5 = 1
        qtd_notas1 = diferenca_unidades
    elif unidade >= 1 and unidade < 5:
        qtd_notas1 = unidade
    elif unidade == 5:
        qtd_notas5 = 1

    return qtd_notas1, qtd_notas5, qtd_notas10, qtd_notas50, qtd_notas100


print(f'Saldo: R${saldo}')

valor_saque = int(input('Informe o valor do saque: '))

if verifica_saldo(saldo, valor_saque):
    saldo_apos_saque = saldo - valor_saque

    nota1, nota5, nota10, nota50, nota100 = calculo_notas_saque(valor_saque)

    print(f'Saque: R${valor_saque}\n'
          f'\nNOTAS ENTREGUES:\n'
          f'Quantidade de notas de 100 reais: {nota100}\n'
          f'Quantidade de notas de 50 reais: {nota50}\n'
          f'Quantidade de notas de 10 reais: {nota10}\n'
          f'Quantidade de notas de 5 reais: {nota5}\n'
          f'Quantidade de notas de 1 real: {nota1}\n'
          f'\nSaldo após saque: {saldo_apos_saque}'
          )
    input("Transação efetuada com sucesso!!!")
    os.system('exit')
elif valor_saque > saldo:
    print('\nSaldo insuficiente!')
else:
    print('\nValor mínimo de R$10 por saque!')
