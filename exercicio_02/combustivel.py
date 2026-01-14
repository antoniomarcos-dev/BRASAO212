"""
Este programa calcula o consumo médio de combustível de um veículo.
"""

# Dados de entrada
distancia_percorrida = 300  # em km
combustivel_gasto = 25    # em litros

# Calcula o consumo médio
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibe os resultados
print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litros")
print(f"Consumo Médio: {consumo_medio:.2f} km/l")
