def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"

try:
    peso_usuario = float(input("Digite seu peso em kg (ultilize ponto como separador): "))
    altura_usuario = float(input("Digite sua altura em metros (ultilize ponto como separador): "))
    
    if peso_usuario <= 0 or altura_usuario <= 0:
        print("Peso e altura devem ser valores positivos.")
    else:
        imc_calculado = calcular_imc(peso_usuario, altura_usuario)
        classificacao = classificar_imc(imc_calculado)
        
        print(f"Seu IMC é: {imc_calculado:.2f}")
        print(f"Classificação: {classificacao}")

except ValueError:
    print("Por favor, digite valores numéricos válidos para peso and altura.")
except ZeroDivisionError:
    print("Altura não pode ser zero.")
