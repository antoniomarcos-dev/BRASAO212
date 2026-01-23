import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta erro para códigos de status HTTP ruins
        data = response.json()
        
        if 'erro' in data:
            print("CEP não encontrado ou inválido.")
        else:
            logradouro = data.get('logradouro', 'Não informado')
            bairro = data.get('bairro', 'Não informado')
            cidade = data.get('localidade', 'Não informado')
            estado = data.get('uf', 'Não informado')
            
            print(f"Logradouro: {logradouro}")
            print(f"Bairro: {bairro}")
            print(f"Cidade: {cidade}")
            print(f"Estado: {estado}")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
    except ValueError:
        print("Erro ao processar a resposta da API.")

if __name__ == "__main__":
    cep = input("Digite o CEP (apenas números): ").strip()
    if cep.isdigit() and len(cep) == 8:
        consultar_cep(cep)
    else:
        print("CEP inválido. Deve conter exatamente 8 dígitos.")
