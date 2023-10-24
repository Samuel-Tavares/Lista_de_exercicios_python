def verificando_par_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


valor = int(input("Informe um número inteiro: "))

if verificando_par_impar(valor):
    print("O valor é par!")
else:
    print("O valor é impar!")
