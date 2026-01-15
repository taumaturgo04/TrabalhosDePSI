import os


def limpar_consola():
    """Limpa a tela da consola para uma melhor visualização."""
    # os.system('cls' if os.name == 'nt' else 'clear')
    pass


def gerar_sigla(frase):
    """Gera uma sigla a partir de uma frase."""
    if not frase:
        return ""
    # Simplified list comprehension to get the first letter of each word and uppercase it
    palavras = frase.strip().split()
    primeiras_letras = [palavra[0].upper() for palavra in palavras if palavra]
    sigla = "".join(primeiras_letras)
    return sigla


def menu_principal_sigla():
    """Menu interativo principal com opções numéricas."""
    limpar_consola()
    print("--- Gerador de Siglas ---")

    while True:  # Loop principal do menu
        print("\nEscolha uma opção:")
        print("1. Inserir uma nova frase")
        print("2. Sair do programa")

        opcao = input("Opção: ")

        if opcao == '1':
            # Lógica para inserir e processar a frase
            frase = input("\nDigite a frase: ")
            if not frase.strip():
                print("A frase não pode estar vazia.")
                continue

            sigla_gerada = gerar_sigla(frase)
            print(f"\nFrase original: '{frase}'")
            print(f"Sigla gerada: **{sigla_gerada}**")

        elif opcao == '2':
            # Sai do loop principal e termina a função
            print("A sair do programa. Até mais!")
            break

        else:
            # Opção inválida
            print("Opção inválida. Por favor, digite '1' ou '2'.")


# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal_sigla()
