# importa a biblioteca de conversão de valores que contém a cotação atual de vários países
from forex_python.converter import CurrencyRates

valor = str(input('Informe o valor da moeda a ser convertida: '))
valor = float(valor.replace(',', '.'))
moeda_origem = input('Informe a moeda de origem: ').upper()
moeda_destino = input('Informe a moeda de destino: ').upper()

# faz a conversão de acordo com a taxa de câmbio do dia
result = CurrencyRates().convert(moeda_origem, moeda_destino, valor)

# exibe o resultado na tela
print(f'$ {valor:,.2f} {moeda_origem} = $ {result:,.2f} {moeda_destino}.')