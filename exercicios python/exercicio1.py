#1. Crie um programa que peça o nome do usuário e imprima uma saudação personalizada.

# Aqui será inserido o nome do usuário e a parte do dia que está
print("==============Seja Bem-vindo==========\n")

# Pede nome e periodo do dia
nome = input("Insira seu nome:")
pdia = input("Está em que periodo do dia(Manhã, tarde, noite)?\n").lower()

# Utlizando as estruturas de condição if/elif/else o periodo do dia que o usuário digitou será depois transformado em saudação
if pdia == "manha" or "manhã":   # Se for manhã, retorna Bom dia
    saudacao = "Bom dia"
elif pdia == "tarde":   # Se for tarde, retorna Boa tarde
    saudacao = "Boa tarde"
elif pdia == "noite":   # Se for noite, retorna Boa noite
    saudacao = "Boa noite"
else:   # Se nenhuma das opções deixa o espaço em branco
    saudacao = " "

# aqui as informações digitadas serão formatadas e assim visualizadas pelo usuário
print("======================================")
print(f"Olá senhor(a) {nome}, {saudacao} seja muito bem-vindo(a)!\n")