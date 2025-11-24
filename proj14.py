inv = ["-" for i in range(10)]

for i in range(10):
    print(inv[i], end=" ")
print()

while True:
    pos = int(input("Escolha posição (1–10): ")) - 1

    if inv[pos] == "-":
        inv[pos] = "X"
    else:
        print("Posição ocupada!")

    for i in range(10):
        print(inv[i], end=" ")
    print()

    cont = input("Continuar? (s/n): ")
    if cont == "n":
        break
