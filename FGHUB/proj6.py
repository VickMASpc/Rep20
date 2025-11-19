import random

resultados = [
    "perdeu",
    "perdeu",
    "ganhou",
    "perdeu",
    "perdeu",
    "perdeu",
    "perdeu"
]

tentativas = 5

print(f"Você tem {tentativas} tentativas")

tentativas = tentativas - 1

while tentativas >= 1:
    print("Jogar?\n1. Sim\n2. Não")
    jogar = (input())
    if jogar == "1" or "sim" or "Sim" or "S" or "s":
        print(f"Você tem {tentativas} tentativas")
        jogada = random.randint(0, 6)
        resultado = resultados[jogada]
        print(f"Você {resultado}!")
        tentativas = tentativas - 1

    elif jogar == "2" or "não" or "Não" or "N" or "n":
        exit

vezGanhou = 0

if resultado == "ganhou":
    vezGanhou = vezGanhou + 1

if tentativas == 0:
    print("Acabaram sua chances!")

print(f"Vezes que ganhou: {vezGanhou}")
