loja_produtos = []


def adicionar_produto():
    try:
        id_p = int(input("ID do produto: "))
        # Verifica se o ID já existe
        if any(p[0] == id_p for p in loja_produtos):
            print("Erro: Já existe um produto com este ID!")
            return

        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        stock = int(input("Quantidade em stock: "))

        loja_produtos.append((id_p, nome, preco, stock))
        print("✓ Produto adicionado com sucesso!")
    except ValueError:
        print("Erro: Insira valores numéricos válidos!")


def listar_todos():
    if not loja_produtos:
        print("\nA loja está vazia.")
    else:
        print("\n" + "=" * 30)
        print("      LISTA DE PRODUTOS")
        print("=" * 30)
        for p in loja_produtos:
            print(f"ID: {p[0]} | Nome: {p[1]:<10} | Preço: {p[2]:>6.2f}€ | Stock: {p[3]}")



def remover_produto():
    try:
        id_remover = int(input("ID do produto a eliminar: "))
        for p in loja_produtos:
            if p[0] == id_remover:
                loja_produtos.remove(p)
                print("✓ Produto removido com sucesso!")
                return
        print("Produto não encontrado.")
    except ValueError:
        print("ID inválido.")


def atualizar_stock():
    try:
        id_p = int(input("ID do produto: "))
        for i, p in enumerate(loja_produtos):
            if p[0] == id_p:
                novo_stock = int(input(f"Novo stock para {p[1]}: "))
                # Atualiza a tupla (tuplas são imutáveis, por isso substituímos a tupla inteira)
                loja_produtos[i] = (p[0], p[1], p[2], novo_stock)
                print("✓ Stock atualizado!")
                return
        print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida.")


# ------------------------------

def procurar_por_id():
    try:
        id_procurado = int(input("Insira o ID a pesquisar: "))
        for p in loja_produtos:
            if p[0] == id_procurado:
                print(f"\nDetalhes: {p[1]}\nPreço: {p[2]}€ | Stock: {p[3]} unidades")
                return
        print("Produto não encontrado.")
    except ValueError:
        print("ID inválido.")


def calcular_patrimonio():
    total = sum(p[2] * p[3] for p in loja_produtos)
    print(f"\nValor total do inventário: {total:.2f}€")


def menu():
    while True:
        print("\n--- GESTÃO DE LOJA ---")
        print("1. Adicionar Produto")
        print("2. Listar Todos")
        print("3. Pesquisar por ID")
        print("4. Atualizar Stock")
        print("5. Remover Produto")
        print("6. Valor Total em Stock")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_todos()
        elif opcao == "3":
            procurar_por_id()
        elif opcao == "4":
            atualizar_stock()
        elif opcao == "5":
            remover_produto()
        elif opcao == "6":
            calcular_patrimonio()
        elif opcao == "0":
            print("A encerrar sistema...")
            break
        else:
            print("⚠Opção inválida!")


if __name__ == "__main__":
    menu()
