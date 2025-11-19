import sys
cardapio = [
    ["Item 1", "Item 1", "Item 1", "Item 1", "Item 1"],
    ["Item 1", "Item 1", "Item 1", "Item 1", "Item 1"],
    ["Item 1", "Item 1", "Item 1", "Item 1", "Item 1"],
    ["Item 1", "Item 1", "Item 1", "Item 1", "Item 1"],
    ["Item 1", "Item 1", "Item 1", "Item 1", "Item 1"]
]

a = 1

while a > 0:
    print(*cardapio[0])
    print(*cardapio[1])
    print(*cardapio[2])
    print(*cardapio[3])
    print(*cardapio[4])
    col = int(input("Coluna: "))
    lin = int(input("Linha: "))

    actCol = col - 1
    actLin = lin - 1

    ed = input("Digite o que quer adicionar: ")

    ned = True

    if cardapio[actLin][actCol] != "Item 1":
        print(f'Este item contém o valor: {cardapio[actLin][actCol]}. Deseja sobrescrever este item? (s/n)')
        a -= 1

        respSob = input()

        if respSob == "s":
            a += 1

        elif respSob == "n":
            ned = False
            a += 1

        else:
            print("Inválido")
            sys.exit(0)

    if ned:
        cardapio[actLin][actCol] = ed

    print(*cardapio[0])
    print(*cardapio[1])
    print(*cardapio[2])
    print(*cardapio[3])
    print(*cardapio[4])
    a -= 1

    if a < 1:
        print("Continuar? (s/n)")

        resp = input()

        if resp == "s":
            a += 1

        elif resp == "n":
            print("Até")
            sys.exit(0)

        else:
            print("Inválido")
            sys.exit(0)
