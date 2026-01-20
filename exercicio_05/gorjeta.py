def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta a ser deixada em um restaurante.

    Parâmetros:
        valor_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta desejada (ex: 10 para 10%).

    Retorna:
        float: O valor da gorjeta a ser pago.
    """
    if valor_conta < 0 or porcentagem_gorjeta < 0:
        raise ValueError("O valor da conta e a porcentagem da gorjeta não podem ser negativos.")
    
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

if __name__ == "__main__":
    try:
        valor_conta = float(input("Digite o valor total da conta: R$ "))
        porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta desejada: "))
        
        gorjeta_calculada = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
        
        print(f"O valor da gorjeta é de R$ {gorjeta_calculada:.2f}")
    
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
