# 20.Crie um programa que simule uma calculadora com as 4 operações básicas.

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
print(num1, operacao, num2)
print("Resultado:", resultado)

