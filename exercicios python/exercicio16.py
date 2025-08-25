#16. Peça ao usuário dois números e exiba todos os números entre eles (inclusive).

# Pede os dois números ao usuário
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# Garante que o menor venha primeiro
if n1 > n2:    #Se num1 for maior que num2, ele inverte os valores.
    n1, n2 = n2, n1   # Aqui será feita a troca dos valores.
    
# Retorna os números inseridos pelo usuário.
print(f"Números entre {n1} e {n2}:")
for i in range(n1, n2 + 1):
    print(i)
