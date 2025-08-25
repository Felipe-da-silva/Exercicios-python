#17.Crie uma função que receba um número e retorne se ele é primo.

# Pede um número ao usuário
num = int(input("Digite um número: "))

# Começa assumindo que o número é primo
primo = True

# Números menores ou iguais a 1 não são primos
if num <= 1:
    primo = False
else:
    # Testa se o número tem algum divisor além de 1 e dele mesmo
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break  # não precisa continuar testando

# Mostra o resultado
if primo == True:
    print(num, "é primo")
else:
    print(num, "não é primo")


