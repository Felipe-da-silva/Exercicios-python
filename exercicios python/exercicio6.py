#6. Solicite três notas e calcule a média. Diga se o aluno foi aprovado (média ≥ 7).

print("Insira as 3 (três) notas do aluno")

soma = 0  # variável para acumular as notas

for i in range(3):
    nota = float(input("Insira a nota: "))
    
# soma todas as notas
    soma += nota

# calcula a média correta
media = soma / 3  

if media >= 7:
    print("O aluno está aprovado")
else:
    print("O aluno está reprovado")
