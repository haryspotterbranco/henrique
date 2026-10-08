boletim = {}

continuar = "s"

while continuar.lower() == "s":
    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    
    boletim[nome] = nota
    
    continuar = input("Deseja adicionar mais um aluno? (s/n): ")

print("\n--- Resultado Final ---")

for aluno, nota in boletim.items():
    if nota >= 6.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
        
    print(f"Aluno(a): {aluno} | Nota: {nota:.1f} | Situação: {situacao}")