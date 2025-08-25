#13. Leia 5 números inteiros e mostre o maior e o menor valor.

# Cria uma lista vazia para guardar os numeros
numero = []

# Mensagem para informando para inserir os números
print("Insira 5 números")

# Pede 5 números ao usuário
for i in range(5):
    numero.append(input("Digite número: ")) # Adiciona cada número à lista
    
    maior = max(numero) # Usa max() para achar o maior valor.
    menor = min(numero) # Usa min() para achar o menor valor.

# Mostra todos os números que foram inseridos e qual é o maior e o menor
print("\nVocê inseriu os seguintes números: ", numero)    
print("O maior número é: ", maior, ". O menor número inserido foi: ", menor, "\n")    