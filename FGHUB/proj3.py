import sys
frutas = []

for i in range(5):
    print("adicionar?")
    print("1. Sim\n2. Não")

    r = int(input())

    if r == 1:
        fruta = input("Adicione uma fruta: ")
        frutas.append(fruta)
        print(*frutas)

    elif r == 2:
        print("Até")
        sys.exit()
