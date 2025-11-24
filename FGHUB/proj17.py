muro = [
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "]
]

while True:
    for linha in muro:
        print(*linha)

    lin = int(input("Linha (1–3): ")) - 1
    col = int(input("Coluna (1–4): ")) - 1

    if muro[lin][col] == " ":
        muro[lin][col] = "▉"
    else:
        print("Já tem um bloco aí!")

    cheio = True
    for linha in muro:
        for c in linha:
            if c == " ":
                cheio = False

    if cheio:
        print("Muro terminado!")
        break
