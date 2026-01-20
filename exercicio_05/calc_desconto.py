def calcular_preco_final(preco_original, percentual_desconto):
    """
    Calcula o preço final de um produto após aplicar um desconto percentual.

    Parâmetros:
        preco_original (float): O preço original do produto.
        percentual_desconto (float): O percentual de desconto a ser aplicado (ex: 15 para 15%).

    Retorna:
        float: O preço final com o desconto aplicado, arredondado para 2 casas decimais.
    """
    if preco_original < 0 or percentual_desconto < 0 or percentual_desconto > 100:
        raise ValueError("O preço e o desconto devem ser valores positivos, e o desconto não pode exceder 100%.")

    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    
    return round(preco_final, 2)

if __name__ == "__main__":
    try:
        # Interação com o usuário para obter os valores
        preco_original_input = float(input("Digite o preço original do produto: R$ "))
        percentual_desconto_input = float(input("Digite o percentual de desconto (%): "))
        
        # Cálculo do preço final usando a função
        preco_com_desconto = calcular_preco_final(preco_original_input, percentual_desconto_input)
        
        # Mostra o resultado formatado
        print(f"\nO preço original era R$ {preco_original_input:.2f}.")
        print(f"Com um desconto de {percentual_desconto_input}%, o preço final é R$ {preco_com_desconto:.2f}.")

    except ValueError as e:
        print(f"Erro nos dados de entrada: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
