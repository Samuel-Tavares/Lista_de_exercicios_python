def turno():
    if resposta == 'M':
        print('\nBom dia!')
    elif resposta == 'V':
        print('\nBoa tarde!')
    elif resposta == 'N':
        print('\nBoa noite!')
    else:
        print('\nResposta inválida, tente novamente!')


resposta = input('Em qual turno você estuda? \n'
                 'Responda com a letra correspondente:\n'
                 '[M] -> Matutino\n'
                 '[V] -> Vespertino\n'
                 '[N] -> Noturno\n'
                 '\nRESPOSTA: '
                 )

resposta = resposta.upper()

turno()
