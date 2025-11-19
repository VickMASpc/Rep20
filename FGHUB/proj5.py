import sys
cinema = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

print(*cinema[0])
print(*cinema[1])
print(*cinema[2])

a = 1

while a > 0:

    if cinema == [
        ["X", "X", "X"],
        ["X", "X", "X"],
        ["X", "X", "X"]
    ]:
        print("Todos os assentos foram comprados")
        sys.exit(0)

    linha = int(input("Digite a LINHA do assento (1, 2 ou 3): "))
    coluna = int(input("Digite a COLUNA do assento (1, 2 ou 3): "))

    actLinha = linha - 1
    actColuna = coluna - 1

    if cinema[actLinha][actColuna] == "X":
        print("Assento já comprado")
    else:
        ed = "X"
        cinema[actLinha][actColuna] = ed

        print(*cinema[0])
        print(*cinema[1])
        print(*cinema[2])

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
