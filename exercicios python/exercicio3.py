#3. Peça um número inteiro e diga se ele é positivo, negativo ou zero.

# Pede ao usuário para digitar um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é maior que 0
if numero > 0:   # Se for maior que 0, o número é positivo
    print("Positivo")
elif numero < 0:  # Verifica se o número é menor que 0
    print("Negativo")   # Se for menor que 0, o número é negativo
else:   # Se não for maior nem menor que 0, só pode ser 0
    print("Zero")   # Mostra que o número é zero

