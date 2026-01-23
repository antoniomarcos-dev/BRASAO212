import requests

def consultar_cambio():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if "USDBRL" in data:
            return data["USDBRL"]
        else:
            print("Erro: Moeda não encontrada na resposta da API.")
            return None
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return None

def main():
    print("--- Consultor de Câmbio USD para BRL ---")
    
    # Busca os dados uma vez para ter a cotação atual
    dados = consultar_cambio()
    
    if dados:
        bid = float(dados['bid'])
        print(f"Cotação atual: 1 {dados['code']} = R$ {bid:.2f}")
        print(f"Última atualização: {dados['create_date']}")
        
        while True:
            print("\n" + "-"*30)
            opcao = input("Deseja realizar uma conversão de USD para BRL? (s/n): ").strip().lower()
            
            if opcao == 's':
                try:
                    valor_usd = float(input("Digite o valor em Dólar (US$): "))
                    valor_brl = valor_usd * bid
                    print(f"Resultado: US$ {valor_usd:.2f} equivale a R$ {valor_brl:.2f}")
                except ValueError:
                    print("Por favor, insira um número válido (use ponto para decimais).")
            elif opcao == 'n':
                print("Encerrando o programa. Até logo!")
                break
            else:
                print("Opção inválida. Digite 's' para sim ou 'n' para não.")

if __name__ == "__main__":
    main()