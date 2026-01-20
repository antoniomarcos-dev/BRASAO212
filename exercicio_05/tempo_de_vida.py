from datetime import date

def calcular_dias_de_vida(data_nascimento):
    """
    Calcula o número de dias entre a data de nascimento e a data atual.

    Parâmetros:
        data_nascimento (date): Um objeto date representando a data de nascimento.

    Retorna:
        int: O número total de dias vividos.
    """
    if data_nascimento > date.today():
        raise ValueError("A data de nascimento não pode ser no futuro.")
        
    delta = date.today() - data_nascimento
    return delta.days

if __name__ == "__main__":
    print("--- Calculadora de Dias de Vida ---")
    try:
        # Pede o dia, mês e ano de nascimento
        ano = int(input("Digite o ano de seu nascimento (ex: 1990): "))
        mes = int(input("Digite o mês de seu nascimento (ex: 7): "))
        dia = int(input("Digite o dia de seu nascimento (ex: 15): "))
        
        # Cria o objeto de data para o nascimento
        data_nascimento = date(ano, mes, dia)
        
        # Calcula os dias de vida usando a função
        dias_vividos = calcular_dias_de_vida(data_nascimento)
        
        # Exibe o resultado
        print(f"\nVocê nasceu em {data_nascimento.strftime('%d/%m/%Y')}.")
        print(f"Até hoje, você já viveu {dias_vividos} dias.")

    except ValueError as e:
        # Trata erros de data inválida (ex: 30 de Fevereiro) ou data no futuro
        print(f"\nErro: Data inválida. {e}")
    except TypeError:
        # Trata erro se a entrada não for um número
        print("\nErro: Por favor, digite apenas números para dia, mês e ano.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")
