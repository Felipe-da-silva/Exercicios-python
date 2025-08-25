#8. Crie um programa que verifique se um número é par ou ímpar.

# Pede ao usuário para digitar um número inteiro e converte para int
n = int(input("Digite um número: "))

# Verifica se o número é divisível por 2 (resto da divisão é 0)
if n % 2 == 0:
    # Se o resto for 0, o número é par
    print("O número é: Par")
else:
    # Se o resto não for 0, o número é ímpar
    print("O número é: Ímpar")

