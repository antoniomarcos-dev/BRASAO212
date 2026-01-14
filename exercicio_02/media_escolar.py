"""
Este programa calcula a média escolar de um aluno.
"""

# Dados de entrada
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Exibe os resultados
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print(f"Média Final: {media:.2f}")

# Verifica a situação do aluno
if media >= 7.0:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")

