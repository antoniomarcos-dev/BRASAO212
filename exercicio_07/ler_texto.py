def ler_arquivo_usuario():
    """
    Lê um arquivo informado pelo usuário e exibe o conteúdo na tela.
    """
    caminho = input("Digite o caminho do arquivo que deseja ler: ")
    
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            print(f"\n--- Conteúdo de {caminho} ---")
            for linha in f:
                # end='' evita que o print adicione uma nova quebra de linha,
                # já que a linha do arquivo já possui uma.
                print(linha, end='')
            print("\n-----------------------------")
            
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Verifique o caminho digitado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    ler_arquivo_usuario()