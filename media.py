notas = {"Ana": 8.5, "Pedro": 6.0, "Maria": 9.0, "João": 5.5}
soma = 0

for nota in notas.values():
    soma += nota

media = soma / len(notas)
print(f"A média geral da turma é: {media:.2f}")