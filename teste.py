import os


def limpar_consola():
    """Limpa a tela da consola."""
    os.system('cls' if os.name == 'nt' else 'clear')


def gerar_sigla(frase):
    """Gera uma sigla ignorando preposições comuns."""
    ignorar = ["de", "do", "da", "dos", "das", "e", "o", "a", "em", "com"]
    palavras = frase.strip().split()
    letras = [p[0].upper() for p in palavras if p.lower() not in ignorar]
    return "".join(letras)


def gerar_codigo(frase):
    """Opção 3: Gera um código numérico baseado nos caracteres da sigla."""
    sigla = gerar_sigla(frase)
    return "-".join([str(ord(c)) for c in sigla])


def gerar_password(frase):
    """Opção 4: Gera uma password segura usando a sigla filtrada."""
    sigla = gerar_sigla(frase)
    substituicoes = {'A': '4', 'E': '3', 'I': '1', 'O': '0', 'S': '5'}

    pass_limpa = "".join([substituicoes.get(c, c) for c in sigla])
    return f"{pass_limpa}#{len(frase)}!"


def menu_principal_sigla():
    while True:
        print("\n--- GERADOR MULTIFUNÇÕES ---")
        print("1. Gerar Sigla (ignora preposições)")
        print("2. Gerar Password")
        print("3. Gerar Código (ASCII)")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao in ['1', '2', '3']:
            frase = input("Digite a frase: ")
            if not frase.strip():
                print("Erro: Frase vazia.")
                print("Erro :abc")
                continue

            if opcao == '1':
                print(f"Sigla: {gerar_sigla(frase)}")
            elif opcao == '3':
                print(f"Código: {gerar_codigo(frase)}")
            elif opcao == '2':
                print(f"Password: {gerar_password(frase)}")

        elif opcao == '4':
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_principal_sigla()


