#7. Leia um número inteiro e mostre a tabuada de 1 a 10 desse número.

# Pede ao usuário um número inteiro para ver a tabuada
n = int(input("Digite um número para ver sua tabuada: "))

# Mostra um título indicando qual tabuada será exibida
print(f"=== Tabuada de {n} ===\n")

# Laço de repetição de 0 até 10
for i in range(11):
    # Mostra cada linha da tabuada: número x multiplicador = resultado
    print(n, " x ", i, "=", n * i)
