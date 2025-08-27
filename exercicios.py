#  -------------------- Exercicio 1 --------------------------

#1. Crie um programa que peça o nome do usuário e imprima uma saudação personalizada.

print("----------------- Exercicio 1 ----------------------\n")

# Mensagem de saudação
print("==============Seja Bem-vindo==========\n")

# Pede nome e periodo do dia
nome = input("Insira seu nome:")
pdia = input("Está em que periodo do dia(Manhã, tarde, noite)?\n").lower()

# Utlizando as estruturas de condição if/elif/else o periodo do dia que o usuário digitou será depois transformado em saudação
if (pdia == "manha") or (pdia == "manhã"):   # Se for manhã, retorna Bom dia
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

#  -------------------- Exercicio 2 --------------------------

#2. Escreva um programa que leia dois números e mostre o maior deles.

print("----------------- Exercicio 2 ----------------------\n")
print("Insira dois números e descubra qual o maior.\n")

# Pede ao usuário o primeiro número e converte para inteiro
n1 = int(input("Digite o primeiro número: "))

# Pede ao usuário o segundo número e converte para inteiro
n2 = int(input("Digite o segundo número: "))

# Verifica qual número é maior ou se são iguais
if n1 > n2:   # Se o primeiro número for maior, mostra ele
    print("O maior número é:", n1)
elif n2 > n1:   # Se o segundo número for maior, mostra ele
    print("O maior número é:", n2)
else:   # Se nenhum for maior, os dois números são iguais
    print("Os dois números são iguais.")


#  -------------------- Exercicio 3 --------------------------

#3. Peça um número inteiro e diga se ele é positivo, negativo ou zero.

print("\n----------------- Exercicio 3 ----------------------\n")
print("Vamos descobrir se um número é positivo, negativo ou zero\n")

# Pede ao usuário para digitar um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é maior que 0
if numero > 0:   # Se for maior que 0, o número é positivo
    print("\nO número é: Positivo")
elif numero < 0:  # Verifica se o número é menor que 0
    print("\nO número é:Negativo")   # Se for menor que 0, o número é negativo
else:   # Se não for maior nem menor que 0, só pode ser 0
    print("\nO número é: Zero")   # Mostra que o número é zero


#  -------------------- Exercicio 4 --------------------------

#4. Receba dois números e calcule a média aritmética entre eles.

print("\n----------------- Exercicio 4 ----------------------\n")
print("Calculando a média aritmética entre dois números: \n")

# Pede ao usuário o primeiro número, "Int" converte para inteiro
n1 = int(input("Digite o primeiro número: "))

# Pede ao usuário o segundo número
n2 = int(input("Digite o segundo número: ")) 

# Calcula a média dos dois números
media = (n1 + n2) / 2

# Mostra o resultado da média
print("A média entre os dois números é", media)


#  -------------------- Exercicio 5 --------------------------

#5. Leia a idade de uma pessoa e diga se ela é maior de idade (18 anos ou mais).

print("\n----------------- Exercicio 5 ----------------------\n")
print("Insira sua idade para saber se é maior de idade:\n")

# Pede ao usuário para digitar a idade
idade = int(input("Digite a sua idade: "))

# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    # Se for maior ou igual a 18, mostra que é maior de idade
    print("Você é maior de idade.")
else:
    # Se for menor que 18, mostra que é menor de idade
    print("Você é menor de idade.")



#  -------------------- Exercicio 6 --------------------------

#6. Solicite três notas e calcule a média. Diga se o aluno foi aprovado (média ≥ 7).

print("\n----------------- Exercicio 6 ----------------------\n")
print("Insira as 3 (três) notas do aluno para saber se está aprovado:\n")

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


#  -------------------- Exercicio 7 --------------------------

#7. Leia um número inteiro e mostre a tabuada de 1 a 10 desse número.

print("\n----------------- Exercicio 7 ----------------------\n")

# Pede ao usuário um número inteiro para ver a tabuada
n = int(input("Digite um número para ver sua tabuada: "))

# Mostra um título indicando qual tabuada será exibida
print(f"=== Tabuada de {n} ===\n")

# Laço de repetição de 0 até 10
for i in range(11):
    # Mostra cada linha da tabuada: número x multiplicador = resultado
    print(n, " x ", i, "=", n * i)


#  -------------------- Exercicio 8 --------------------------

#8. Crie um programa que verifique se um número é par ou ímpar.

print("\n----------------- Exercicio 8 ----------------------\n")
print("É par ou impar?\n")

# Pede ao usuário para digitar um número inteiro e converte para int
n = int(input("Digite um número: "))

# Verifica se o número é divisível por 2 (resto da divisão é 0)
if n % 2 == 0:
    # Se o resto for 0, o número é par
    print("O número é: Par")
else:
    # Se o resto não for 0, o número é ímpar
    print("O número é: Ímpar")


#  -------------------- Exercicio 9 --------------------------

#9. Peça ao usuário um número e mostre todos os números de 1 até ele.

print("\n----------------- Exercicio 9 ----------------------\n")
print("Insira um número para ver a sequência dos números até ele:\n")

# Pede ao usuário para digitar um número inteiro
n = int(input("Digite um número: "))

# Mostra os números de 1 até n
for i in range(1, n + 1):
    print(i)

#  -------------------- Exercicio 10 --------------------------

#10. Solicite um número e mostre a soma de todos os números pares até ele.

print("\n----------------- Exercicio 10 ----------------------\n")
print("Descubra a sequência dos números pares até o número digitado:\n")

# Variável que vai guardar a soma dos números pares
soma = 0

# Pede ao usuário para digitar um número inteiro
n = int(input("Digite um número: "))

print("\nSequência dos números pares até", n, ":")
for i in range(2, n+1, 2):
    print(i, end=" ")  # mostra cada número par na mesma linha
    soma += i

# Pula uma linha após a sequência
print("\n")

# Mostra o resultado final da soma de todos os números pares
print("A soma dos pares é:", soma)


#  -------------------- Exercicio 11 --------------------------

#11.Crie um programa que leia uma senha até que o usuário acerte a senha correta ('1234').

print("\n----------------- Exercicio 11 ----------------------\n")
print("Adivinhe qual a senha correta.\n")

# Inicializa a variável senha vazia
senha = ' '

# Mensagem de boas-vindas
print("Seja bem-vindo(a)")

# Enquanto a senha digitada for diferente de '1234', continua pedindo
while senha != '1234':
    senha = input("Digite a senha correta:")  # Pede a senha ao usuário

# Quando a senha estiver correta, mostra esta mensagem
print("Senha correta!")


#  -------------------- Exercicio 12 --------------------------

#12. Solicite 5 nomes ao usuário e armazene-os em uma lista. Depois, exiba todos.

print("\n----------------- Exercicio 12 ----------------------\n")
print("Crie uma lista de nomes:\n")

# Cria uma lista vazia para guardar os nomes
nome = []

# Pede 5 nomes ao usuário
for i in range(5):
    nome.append(input("Insira nome:"))  # Adiciona cada nome à lista

# Mostra todos os nomes que foram inseridos
print("Os nomes inseridos foram:", nome)


#  -------------------- Exercicio 13 --------------------------

#13. Leia 5 números inteiros e mostre o maior e o menor valor.

print("\n----------------- Exercicio 13 ----------------------\n")
print("Maior e menor valor de 5 números:\n")

# Cria uma lista vazia para guardar os numeros
numero = []

# Mensagem para informando para inserir os números
print("Insira 5 números")

# Pede 5 números ao usuário
for i in range(5):
    numero.append(int(input("Digite número: "))) # Adiciona cada número à lista
    
    maior = max(numero) # Usa max() para achar o maior valor.
    menor = min(numero) # Usa min() para achar o menor valor.

# Mostra todos os números que foram inseridos e qual é o maior e o menor
print("\nVocê inseriu os seguintes números: ", numero)    
print("O maior número é: ", maior, ". O menor número inserido foi: ", menor, "\n")    


#  -------------------- Exercicio 14 --------------------------

#14. Peça ao usuário para digitar uma palavra e mostre quantas letras ela tem.

print("----------------- Exercicio 14 ----------------------\n")
print("Insira uma palavra e saiba quantas letras ela tem:\n")

# Será inserida a palavra
palavra = input("Digite uma palavra: ")

# Mostra a palavra e o número de letras que há.
print("a palavra inserida foi: ", palavra, " e tem: ", len(palavra), " letras") # 'Len' retorna o tamanho da string


#  -------------------- Exercicio 15 --------------------------

#15.Crie um dicionário com os dados de uma pessoa (nome, idade, cidade) e exiba-os.

print("\n----------------- Exercicio 15 ----------------------\n")
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


#  -------------------- Exercicio 16 --------------------------

#16. Peça ao usuário dois números e exiba todos os números entre eles (inclusive).

print("\n----------------- Exercicio 16 ----------------------\n")
print("Insira dois números para saber quais os números entre eles:\n ")

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


#  -------------------- Exercicio 17 --------------------------

#17.Crie uma função que receba um número e retorne se ele é primo.

print("\n----------------- Exercicio 17 ----------------------\n")
print("Insira um número e descubra se ele é um número primo:")
# Pede um número ao usuário
num = int(input("Digite um número: "))

# Verifica apenas se o número é maior que 1 (pois 0 e 1 não são primos)
if num > 1:
    # Testa se o número tem algum divisor além de 1 e dele mesmo
    for i in range(2, num):
        if num % i == 0:          # Se for divisível por 'i'
            print(num, "não é primo")
            break                 # Sai do laço, pois já não é primo
    else:
        # O 'else' do 'for' só executa se o laço NÃO foi interrompido pelo 'break'
        print(num, "é primo")
else:
    # Caso o número seja menor ou igual a 1
    print(num, "não é primo")



#  -------------------- Exercicio 18 --------------------------

#18. Solicite ao usuário uma frase e exiba-a ao contrário.

print("\n----------------- Exercicio 18 ----------------------\n")
print("Como fica uma frase ao contrário?\n")

# Pede uma frase ao usuário
frase = input("Digite uma frase: ")

print("\n=============> Resultado <=============\n")
# Mostra a frase ao contrário
print("===> Frase invertida:", frase[::-1]) # frase[::-1] ou string[inicio:fim:passo] é uma forma rápida de inverter a string.


#  -------------------- Exercicio 19 --------------------------

#19. Peça ao usuário uma lista de 5 números e mostre a média aritmética.

print("\n----------------- Exercicio 19 ----------------------\n")
print("Insira 5 números e saiba a média aritmética deles:\n")

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


#  -------------------- Exercicio 20 --------------------------

# 20.Crie um programa que simule uma calculadora com as 4 operações básicas.

print("\n----------------- Exercicio 20 ----------------------\n")
print("================== Calculadora =======================\n")
# Pede dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Pede a operação
operacao = input("Digite a operação (+, -, *, /): ")

# Faz a operação escolhida
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operação inválida!"

# Mostra a operação e o resultado.
print("========================================================\n")
print(f"Cálculo: {num1}{operacao}{num2}")

print("Resultado:", resultado)


