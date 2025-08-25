#12. Solicite 5 nomes ao usuário e armazene-os em uma lista. Depois, exiba todos.

# Cria uma lista vazia para guardar os nomes
nome = []

# Pede 5 nomes ao usuário
for i in range(5):
    nome.append(input("Insira nome:"))  # Adiciona cada nome à lista

# Mostra todos os nomes que foram inseridos
print("Os nomes inseridos foram:", nome)
