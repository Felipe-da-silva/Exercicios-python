#2. Escreva um programa que leia dois números e mostre o maior deles.

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