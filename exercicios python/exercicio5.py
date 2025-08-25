#5. Leia a idade de uma pessoa e diga se ela é maior de idade (18 anos ou mais).

# Pede ao usuário para digitar a idade
idade = int(input("Digite a sua idade: "))

# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    # Se for maior ou igual a 18, mostra que é maior de idade
    print("Você é maior de idade.")
else:
    # Se for menor que 18, mostra que é menor de idade
    print("Você é menor de idade.")

