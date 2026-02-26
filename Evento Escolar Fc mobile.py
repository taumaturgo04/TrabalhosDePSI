# 1. SET: Registo de IDs únicos (Garante que ninguém se inscreve duas vezes)
alunos_inscritos = set()

# 2. LISTA: Armazena as inscrições por ordem de chegada
lista_torneio = []


def menu():
    print("\n" + "=" * 30)
    print(" SISTEMA: EVENTO FC MOBILE ")
    print("=" * 30)
    print("1. Inscrever Aluno")
    print("2. Ver Lista de Participantes")
    print("3. Gerar Próximo Jogo")
    print("4. Sair")
    return input("Escolha uma opção: ")


def inscrever():
    try:
        # Pedir dados ao utilizador
        id_aluno = int(input("Número de Processo (ID): "))

        # Validação com SET (O erro mais comum é duplicar inscritos)
        if id_aluno in alunos_inscritos:
            print("\n[ERRO] Este aluno já está inscrito no torneio!")
            return

        nome = input("Nome do Treinador (FC Mobile): ")
        ger = int(input("GER da Equipa (Rating): "))

        # 3. TUPLO: Agrupa os dados que não vão mudar (Imutabilidade)
        participante = (id_aluno, nome, ger)

        # Adicionar às estruturas
        lista_torneio.append(participante)
        alunos_inscritos.add(id_aluno)

        print(f"\n[SUCESSO] {nome} inscrito com sucesso!")

    except ValueError:
        print("\n[ERRO] Introduza apenas números no ID e no GER!")


def mostrar_lista():
    if not lista_torneio:
        print("\n[AVISO] Ainda não há alunos inscritos.")
    else:
        print("\n--- LISTA DE INSCRITOS ---")
        for i, (id_a, nome, ger) in enumerate(lista_torneio, 1):
            print(f"{i}. {nome} | ID: {id_a} | GER: {ger}")


# Ciclo Principal (Main Loop)
while True:
    opcao = menu()

    if opcao == "1":
        inscrever()
    elif opcao == "2":
        mostrar_lista()
    elif opcao == "3":
        if len(lista_torneio) < 2:
            print("\n[ERRO] Precisas de pelo menos 2 alunos para gerar um jogo!")
        else:
            # Exemplo de como usar a LISTA para criar um confronto
            p1 = lista_torneio[0]  # Primeiro da lista
            p2 = lista_torneio[1]  # Segundo da lista
            print(f"\n--- PRÓXIMO CONFRONTO ---")
            print(f"{p1[1]} (GER {p1[2]}) VS {p2[1]} (GER {p2[2]})")
    elif opcao == "4":
        print("A fechar sistema do torneio...")
        break
    else:
        print("\n[ERRO] Opção inválida, tenta novamente.")


