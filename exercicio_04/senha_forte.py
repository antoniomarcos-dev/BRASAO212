import re

def verificar_forca_senha(senha):
    """
    Verifica a força de uma senha com base em critérios de segurança.
    """
    erros = []

    # Critério 1: Comprimento mínimo de 8 caracteres
    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")

    # Critério 2: Pelo menos uma letra minúscula
    if not re.search(r"[a-z]", senha):
        erros.append("A senha deve conter pelo menos uma letra minúscula.")

    # Critério 3: Pelo menos uma letra maiúscula
    if not re.search(r"[A-Z]", senha):
        erros.append("A senha deve conter pelo menos uma letra maiúscula.")

    # Critério 4: Pelo menos um número
    if not re.search(r"\d", senha):
        erros.append("A senha deve conter pelo menos um número.")

    # Critério 5: Pelo menos um caractere especial
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        erros.append("A senha deve conter pelo menos um caractere especial (ex: !@#$%).")

    return erros

def main():
    """
    Função principal que solicita a senha e exibe o resultado da verificação.
    """
    senha = input("Digite a senha que deseja verificar: ")
    erros_encontrados = verificar_forca_senha(senha)

    print("\n--- Análise da Senha ---")
    if not erros_encontrados:
        print("✅ Senha forte!")
    else:
        print("❌ Senha fraca. Por favor, corrija os seguintes pontos:")
        for erro in erros_encontrados:
            print(f"- {erro}")

if __name__ == "__main__":
    main()
