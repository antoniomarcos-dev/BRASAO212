def classificar_idade(idade):
    if 0 <= idade <= 12:
        return "Criança"
    elif 13 <= idade <= 17:
        return "Adolescente"
    elif 18 <= idade <= 59:
        return "Adulto"
    elif idade >= 60:
        return "Idoso"
    else:
        return "Idade inválida"

try:
    idade_usuario = int(input("Digite sua idade: "))
    categoria = classificar_idade(idade_usuario)
    print(f"Você é classificado como: {categoria}")
except ValueError:
    print("Por favor, digite um número válido para a idade.")
