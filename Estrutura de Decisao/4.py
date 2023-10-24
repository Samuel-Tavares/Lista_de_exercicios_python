def vogal_consoante():
    if caractere in ("a", "à", "á", "â", "ã", "e", "è", "é", "ê", "i", "î",
                     "ì", "í", "o", "ò", "ó", "ô", "õ", "u", "ù", "ú", "û"):
        print('O caractere digitado é uma vogal!')
    elif caractere in ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                       "p", "q", "r", "s", "t", "v", "w", "x", "z", "ç"):
        print('A letra digitada é consoante!')
    else:
        print('O caractere digitado não é vogal e nem consoante!')


caractere = input('Informe uma letra e te avisaremos se é Vogal'
                  'ou consoante: ')

caractere = caractere.lower()

vogal_consoante()
