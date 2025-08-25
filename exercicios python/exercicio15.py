#15.Crie um dicionário com os dados de uma pessoa (nome, idade, cidade) e exiba-os.

print("=== Preencha este pequeno questionário ===\n")

# Serão inseridos dados
pessoa = {
    "nome": input("Digite seu nome: "),
    "idade": int(input("Digite sua idade: ")),
    "cidade": input("Digite a sua cidade: ")
}

# Exibindo os dados
print("\n======================")
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

