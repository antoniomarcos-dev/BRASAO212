def eh_ano_bissexto(ano):
    """
    Verifica se um ano é bissexto de acordo com as regras do calendário gregoriano.
    Um ano é bissexto se for divisível por 4, exceto para anos que são
    divisíveis por 100, a menos que também sejam divisíveis por 400.
    """
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        ano_usuario = int(input("Digite um ano para verificar se é bissexto: "))
        
        if ano_usuario <= 0:
            print("Por favor, insira um ano válido (número positivo).")
        else:
            if eh_ano_bissexto(ano_usuario):
                print(f"O ano {ano_usuario} é bissexto.")
            else:
                print(f"O ano {ano_usuario} não é bissexto.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para o ano.")

if __name__ == "__main__":
    main()
