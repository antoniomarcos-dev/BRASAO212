"""
Este programa converte um valor em reais para dólares e euros.
"""

# Dados de entrada
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Calcula os valores convertidos
valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro

# Exibe os resultados formatados
print(f"O valor de R$ {valor_reais:.2f} em dólares é US$ {valor_dolares:.2f}")
print(f"O valor de R$ {valor_reais:.2f} em euros é € {valor_euros:.2f}")
