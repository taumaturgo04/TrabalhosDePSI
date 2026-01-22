quantidade = int(input("Quantas notas quer inserir? "))

notas = []

for i in range(quantidade):
    while True:

        nota = float(input(f"Insira a nota {i + 1} (0-20): "))

        if 0 <= nota <= 20:
            notas.append(nota)
            break
        else:
            print("erro: por favor, insira um valor entre 0 e 20")

nota_maxima = max(notas)
nota_minima = min(notas)
media = sum(notas) / len(notas)

print("\n--- Estatísticas das Notas ---")
print(f"Todas as notas inseridas: {notas}")
print(f"Nota mais alta: {nota_maxima}")
print(f"Nota mais baixa: {nota_minima}")
print(f"Média das notas: {media:.2f}")

