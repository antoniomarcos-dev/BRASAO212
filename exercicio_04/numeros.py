def analisar_numeros():
    """
    Analisa números digitados pelo usuário, classificando-os como pares ou
    ímpares e contabilizando a quantidade de cada um.
    """
    pares = 0
    impares = 0
    
    print("Digite os números para análise. Digite 'sair' para terminar.")

    while True:
        entrada = input("Digite um número (ou 'sair'): ")

        if entrada.lower() == 'sair':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é um número PAR.")
                pares += 1
            else:
                print(f"{numero} é um número ÍMPAR.")
                impares += 1
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro ou 'sair'.")

    print("\n--- Contagem Final ---")
    print(f"Total de números pares inseridos: {pares}")
    print(f"Total de números ímpares inseridos: {impares}")

if __name__ == "__main__":
    analisar_numeros()
