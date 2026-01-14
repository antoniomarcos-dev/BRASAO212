"""
Este programa calcula o desconto de um produto e seu preço final.
"""

# Dados de entrada
nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

# Calcula o valor do desconto e o preço final
valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibe os resultados
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {percentual_desconto}%")
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")
