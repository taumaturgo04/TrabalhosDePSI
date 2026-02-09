import json
import os

FILE_NAME = "turma_1a.json"


# --- LÓGICA DE DADOS (PERSISTÊNCIA) ---

def carregar_dados():
    """Lê o ficheiro JSON e converte chaves para inteiro."""
    if not os.path.exists(FILE_NAME):
        return {}
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return {int(k): v for k, v in dados.items()}
    except (json.JSONDecodeError, ValueError):
        return {}


def guardar_dados(turma):
    """Guarda o dicionário da turma no ficheiro JSON."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(turma, f, indent=4, ensure_ascii=False)


# --- FUNÇÕES DE INTERFACE E UTILITÁRIOS ---

def exibir_cabecalho(titulo):
    print(f"\n{'═' * 45}")
    print(f" {titulo.center(43)}")
    print(f"{'═' * 45}")


def exibir_menu():
    exibir_cabecalho("SISTEMA INOVAR - TURMA 1A")
    print("1. [ + ] Adicionar Aluno")
    print("2. [ L ] Listagem e Resumo")
    print("3. [ ! ] Registar Falta (J / I / D)")
    print("4. [ - ] Remover Última Falta")
    print("5. [ % ] Estatísticas e Métricas")
    print("0. [ X ] Sair e Guardar")
    return input("\nEscolha uma opção: ")


# --- LÓGICA PRINCIPAL ---

def sistema_gestao():
    turma = carregar_dados()

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            try:
                num = int(input("Nº do aluno: "))
                if num in turma:
                    print(">> Erro: Esse número já existe!")
                    continue

                nome = input("Nome: ").strip().title()
                idade = int(input("Idade: "))
                turma[num] = {'nome': nome, 'idade': idade, 'faltas': []}
                print(f">> Aluno {nome} adicionado com sucesso!")
            except ValueError:
                print(">> Erro: Introduza valores numéricos válidos.")

        elif opcao == "2":
            exibir_cabecalho("LISTA DE ALUNOS")
            print(f"{'Nº':<4} | {'Nome':<20} | {'Idade':<5} | {'Faltas (J-I-D)'}")
            print("-" * 55)
            for num, info in sorted(turma.items()):
                f = info['faltas']
                resumo = f"{f.count('J')}J - {f.count('I')}I - {f.count('D')}D"
                print(f"{num:<4} | {info['nome']:<20} | {info['idade']:<5} | {resumo}")

        elif opcao == "3":
            try:
                num = int(input("Nº do aluno: "))
                if num in turma:
                    tipo = input("Tipo ([J]ustificada, [I]njustificada, [D]isciplinar): ").upper()
                    if tipo in ['J', 'I', 'D']:
                        turma[num]['faltas'].append(tipo)
                        print(">> Falta registada.")
                    else:
                        print(">> Tipo de falta inválido.")
                else:
                    print(">> Erro: Aluno não encontrado.")
            except ValueError:
                print(">> Erro: Número inválido.")

        elif opcao == "4":
            try:
                num = int(input("Nº do aluno: "))
                if num in turma and turma[num]['faltas']:
                    removida = turma[num]['faltas'].pop()
                    print(f">> Última falta ({removida}) removida!")
                else:
                    print(">> O aluno não existe ou não possui faltas.")
            except ValueError:
                print(">> Erro: Número inválido.")

        elif opcao == "5":
            if not turma:
                print(">> A turma ainda não tem alunos.")
                continue

            total = len(turma)
            media_idade = sum(a['idade'] for a in turma.values()) / total
            all_f = [f for a in turma.values() for f in a['faltas']]

            j, i, d = all_f.count('J'), all_f.count('I'), all_f.count('D')

            exibir_cabecalho("MÉTRICAS DA TURMA")
            print(f"Total de Alunos: {total}")
            print(f"Média de Idades: {media_idade:.1f} anos")
            print(f"Total de Faltas: {len(all_f)}")
            print("\nDistribuição Visual:")
            print(f"  Justificadas:   {'█' * j} ({j})")
            print(f"  Injustificadas: {'█' * i} ({i})")
            print(f"  Disciplinares:  {'█' * d} ({d})")

        elif opcao == "0":
            guardar_dados(turma)
            print("\n>> Dados guardados. A encerrar o sistema...")
            break

        else:
            print(">> Opção inválida! Tente novamente.")


if __name__ == "__main__":
    sistema_gestao()
