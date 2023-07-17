print('| CONVERSOR DE FAHRENHEIT PARA CELSIUS |')

fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))

celsius = ((fahrenheit - 32) * 5 / 9)
print('A temperatura em Celsius é: ' + str(celsius))

input('Tecle "Enter" para sair...')
