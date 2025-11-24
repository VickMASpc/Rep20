secret = 7
tentativa = 0

print("Adivinhe o número!")

while tentativa != secret:
    tentativa = int(input("Digite um número: "))

    if tentativa < secret:
        print("Muito baixo!")
    elif tentativa > secret:
        print("Muito alto!")
    else:
        print("Acertou!")
