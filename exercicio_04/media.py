def avaliar_satisfacao(media):
    if 9 <= media <= 10:
        return "Excelente"
    elif 8 <= media < 9:
        return "Ótima"
    elif 6 <= media < 8:
        return "Boa"
    elif 4 <= media < 6:
        return "Regular"
    elif 2 <= media < 4:
        return "Ruim"
    else:
        return "Péssima"

def registrar_notas_e_calcular_media():
    """
    Registra as notas dos alunos e calcula a média da turma.
    """
    notas = []
    print("Digite as notas dos alunos. Digite 'fim' para concluir.")

    while True:
        entrada = input(f"Digite a nota do aluno {len(notas) + 1} (ou 'fim'): ")

        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Por favor, insira um valor entre 0 and 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número ou 'fim'.")

    if not notas:
        print("\nNenhuma nota foi inserida.")
        return

    media = sum(notas) / len(notas)
    satisfacao = avaliar_satisfacao(media)

    print("\n--- Resultados ---")
    print("Notas registradas:", notas)
    print(f"A média da turma é: {media:.2f}")
    print(f"Nível de satisfação da turma: {satisfacao}")

if __name__ == "__main__":
    registrar_notas_e_calcular_media()
