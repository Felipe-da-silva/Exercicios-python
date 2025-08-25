#10. Solicite um número e mostre a soma de todos os números pares até ele.

# Variável que vai guardar a soma dos números pares
soma = 0

# Pede ao usuário para digitar um número inteiro
n = int(input("Digite um número: "))

'''
Percorre todos os números pares de 2 até n
O último '2' no range significa que vai de 2 em 2
'''
for i in range(2, n+1, 2):
    soma += i  # Adiciona o número atual à soma

# Mostra o último número par percorrido
print(i)

# Mostra o resultado final da soma de todos os números pares
print("A soma dos pares é:", soma)

