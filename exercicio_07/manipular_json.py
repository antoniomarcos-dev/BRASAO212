import json

def manipular_dados_json():
    """
    Salva um dicionário em um arquivo JSON e depois lê o mesmo arquivo.
    """
    # Dicionário com os dados
    pessoa = {
        "nome": "João Pereira",
        "idade": 30,
        "cidade": "Porto Alegre"
    }
    
    arquivo_json = "dados_pessoa.json"
    
    # Escrita do arquivo
    try:
        with open(arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(pessoa, f, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em '{arquivo_json}'.")
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")
        return

    # Leitura do arquivo
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            dados_lidos = json.load(f)
        
        print("\nDados lidos do arquivo:")
        print(dados_lidos)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_json}' não existe.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    manipular_dados_json()