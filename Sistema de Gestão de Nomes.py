def exibir_menu():
    print("\n--- SISTEMA DE GESTÃO DE NOMES ---")
    print("1. Adicionar nome")
    print("2. Remover nome")
    print("3. Listar todos os nomes")
    print("4. Procurar um nome")
    print("0. Sair")
    return input("Escolha uma opção: ")


def gerir_nomes():
    nomes = []

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            nome = input("Digite o nome a adicionar: ").strip()
            if nome:
                nomes.append(nome)
                print(f"'{nome}' foi adicionado com sucesso!")
            else:
                print("Erro: O nome não pode estar vazio.")

        elif opcao == "2":
            nome = input("Digite o nome a remover: ").strip()
            if nome in nomes:
                nomes.remove(nome)
                print(f"'{nome}' foi removido.")
            else:
                print("Erro: Nome não encontrado na lista.")

        elif opcao == "3":
            print("\n--- LISTA DE NOMES ---")
            if not nomes:
                print("A lista está vazia.")
            else:
                for i, n in enumerate(sorted(nomes), 1):
                    print(f"{i}. {n}")

        elif opcao == "4":
            nome = input("Digite o nome que deseja procurar: ").strip()
            if nome in nomes:
                posicao = nomes.index(nome)
                print(f"O nome '{nome}' foi encontrado na posição {posicao + 1}.")
            else:
                print(f"O nome '{nome}' não existe na lista.")

        elif opcao == "0":
            print("A encerrar o programa... Até breve!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    gerir_nomes()
