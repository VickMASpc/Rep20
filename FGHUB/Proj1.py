import sys
import random

print("Bem vindo")

camp = [
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
]

print(*camp[0])
print(*camp[1])
print(*camp[2])
print(*camp[3])
print(*camp[4])
print(*camp[5])
print(*camp[6])

randLin = random.randint(0, 6)
randCol = random.randint(0, 11)

tries = 0
wins = 0

camp[randLin][randCol] = "X"

a = 1

while a > 0:

    guessLin = int(input("Escolha uma linha: "))

    actGuessLin = guessLin - 1

    guessCol = int(input("Escolha uma coluna: "))

    tries += 1

    print(camp[actGuessLin][guessCol])

    if camp[actGuessLin][guessCol] == "X":
        print("Você Acertou!")
        wins += 1

    elif camp[actGuessLin][guessCol] == "O":
        print("Campo já marcado")
        tries -= 1

    elif camp[actGuessLin][guessCol] == "-":
        print("Você errou")

    else:
        print("???")

    camp[actGuessLin][guessCol] = "O"

    print(f'Tentativas: {tries}')
    print(f'Vitórias: {wins}')

    print("Continuar? (s/n)")

    cont = input()

    if cont == "n":
        a -= 1
        print("Até")
        sys.exit()

    elif cont == "s":
        a = 1

    else:
        print("input inválido, tente novamente")

        print("Continuar? (s/n)")

        cont = input()
