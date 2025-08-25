#19. Peça ao usuário uma lista de 5 números e mostre a média aritmética.

# Lista para guardar os números
numeros = []

# Pede 5 números ao usuário
for i in range(5):
    numeros.append(float(input(f"Digite o {i+1}º número: ")))

# Calcula a média
media = sum(numeros) / len(numeros) # sum(numeros) soma todos os números da lista. len(numeros) lê quantidade de números na lista (neste caso, 5).

# Mostra os números inseridos
print("Você digitou os números:", numeros)
print("A média dos números é:", media) # Mostra o resultado