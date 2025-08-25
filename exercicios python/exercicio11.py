#11.Crie um programa que leia uma senha até que o usuário acerte a senha correta ('1234').

# Inicializa a variável senha vazia
senha = ' '

# Mensagem de boas-vindas
print("Seja bem-vindo(a)")

# Enquanto a senha digitada for diferente de '1234', continua pedindo
while senha != '1234':
    senha = input("Digite a senha correta:")  # Pede a senha ao usuário

# Quando a senha estiver correta, mostra esta mensagem
print("Senha correta!")
