import csv
import re

def converter_para_dias(tempo_str):
    """Converte a string de tempo (anos, meses, dias) para um total estimado de dias."""
    # Padrão: "X anos, Y meses e Z dias"
    match = re.search(r"(\d+) anos, (\d+) meses e (\d+) dias", tempo_str)
    if match:
        anos, meses, dias = map(int, match.groups())
        # Estimativa: 1 ano = 365 dias, 1 mês = 30 dias
        return (anos * 365) + (meses * 30) + dias
    return None

def analisar_tempo_execucao():
    """
    Lê um arquivo CSV e calcula a média e o máximo da coluna 'tempo_execucao'.
    """
    arquivo = input("Digite o caminho do arquivo CSV: ")
    
    tempos = []
    
    try:
        with open(arquivo, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            
            for linha in leitor:
                # Verifica se a coluna existe e se o valor é numérico
                if 'tempo_execucao' in linha and linha['tempo_execucao']:
                    texto_tempo = linha['tempo_execucao']
                    try:
                        valor = float(texto_tempo)
                        tempos.append(valor)
                    except ValueError:
                        dias = converter_para_dias(texto_tempo)
                        if dias is not None:
                            tempos.append(dias)
        
        if tempos:
            media = sum(tempos) / len(tempos)
            maximo = max(tempos)
            print(f"\nAnálise da coluna 'tempo_execucao' (em dias estimados):")
            print(f"Média: {media:.2f} dias")
            print(f"Máximo: {maximo:.2f} dias")
        else:
            print("Não foram encontrados dados válidos na coluna 'tempo_execucao'.")
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    analisar_tempo_execucao()