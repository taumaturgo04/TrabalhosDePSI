import json
import os

FILE_NAME = "turma_1a.json"


def carregar_dados():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:

            dados = json.load(f)
            return {int(k): v for k, v in dados.items()}
    return {}


def guardar_dados(turma):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(turma, f, indent=4, ensure_ascii=False)


def exibir_menu():
    print("\n" + "═" * 40)
    print("      SISTEMA INOVAR - TURMA 1A")
    print("" + "═" * 40)
    print("1. Adicionar Aluno")
    print("2. Ver Lista Completa e Resumo")
    print("3. Registar Falta (J / I / D)")
    print("4. Remover Última Falta")
    print("5. Estatísticas da Turma (Métricas)")
    print("0. Sair e Guardar")
    return input("\nEscolha uma opção: ")


def sistema_gestao():
    turma_1a = carregar_dados()

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            try:
                num = int(input("Nº do aluno: "))
                if num in turma_1a:
                    print("Erro: Esse número já existe!")
                    continue
                nome = input("Nome: ").strip().title()
                idade = int(input("Idade: "))

                turma_1a[num] = {'nome': nome, 'idade': idade, 'faltas': []}
                print(f"{nome} adicionado!")
            except ValueError:
                print("Erro: Introduza valores válidos.")

        elif opcao == "2":
            print(f"\n{'Nº':<4} | {'Nome':<20} | {'Idade':<5} | {'Faltas (J-I-D)'}")
            print("-" * 50)
            for num, info in sorted(turma_1a.items()):
                f = info['faltas']
                resumo = f"{f.count('J')}J - {f.count('I')}I - {f.count('D')}D"
                print(f"{num:<4} | {info['nome']:<20} | {info['idade']:<5} | {resumo}")

        elif opcao == "3":
            try:
                num = int(input("Nº do aluno: "))
                if num in turma_1a:
                    tipo = input("Tipo [J]ustificada, [I]njustificada, [D]isciplinar: ").upper()
                    if tipo in ['J', 'I', 'D']:
                        turma_1a[num]['faltas'].append(tipo)
                        print("Falta registada.")
                    else:
                        print("Tipo inválido.")
                else:
                    print(" Aluno não encontrado.")
            except ValueError:
                print(" Erro no número.")

        elif opcao == "5":
            if not turma_1a:
                print("Turma vazia.")
                continue
            media_idade = sum(a['idade'] for a in turma_1a.values()) / len(turma_1a)
            total_faltas = sum(len(a['faltas']) for a in turma_1a.values())
            print(f"\n--- MÉTRICAS DA TURMA ---")
            print(f"Total de Alunos: {len(turma_1a)}")
            print(f"Média de Idades: {media_idade:.1f} anos")
            print(f"Total de Faltas: {total_faltas}")

        elif opcao == "0":
            guardar_dados(turma_1a)
            print(" Dados guardados. A encerrar...")
            break
        else:
            print("⚠  Opção inválida!")


if __name__ == "__main__":
    sistema_gestao()
