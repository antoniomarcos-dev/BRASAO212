import string

def verificar_palindromo(frase):
    """
    Verifica se uma palavra ou frase é um palíndromo.

    Parâmetros:
        frase (str): A palavra ou frase a ser verificada.

    Retorna:
        str: "Sim" se for um palíndromo, "Não" caso contrário.
    """
    # Remove espaços e pontuações e converte para minúsculas
    frase_limpa = ''.join(char.lower() for char in frase if char.isalnum())
    
    # Verifica se a frase limpa é igual à sua inversa
    if frase_limpa == frase_limpa[::-1]:
        return "Sim"
    else:
        return "Não"

if __name__ == "__main__":
    try:
        texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
        resultado = verificar_palindromo(texto)
        print(f"A entrada é um palíndromo? {resultado}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
