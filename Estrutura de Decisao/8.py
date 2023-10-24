preco1 = float(input('Preço do 1° produto: '))
preco2 = float(input('Preço do 2° produto: '))
preco3 = float(input('Preço do 3° produto: '))

print('-'*40)


def menor_valor():
    if preco1 < preco2 and preco1 < preco3:
        print('O 1° produto tem o menor valor!')
    elif preco2 < preco1 and preco2 < preco3:
        print('O 2° produto tem o menor valor!')
    elif preco3 < preco1 and preco3 < preco2:
        print('O 3° produto tem o menor valor!')
    elif preco1 == preco2 and preco1 < preco3:
        print('O 1° e 2° produto são os mais baratos '
              'e possuem o memso valor!'
              )
    elif preco1 == preco3 and preco1 < preco2:
        print('O 1° e 3° produto são os mais baratos '
              'e possuem o mesmo valor!'
              )
    elif preco3 == preco2 and preco3 < preco1:
        print('O 2° e 3° produto são os mais baratos '
              'e possuem o mesmo valor!'
              )
    else:
        print('Todos possuem os produtos possuem o mesmo valor!')


menor_valor()
