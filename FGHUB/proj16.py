campo = [
    ["?", "?", "?", "?"],
    ["?", "?", "?", "?"],
    ["?", "?", "?", "?"],
    ["?", "?", "?", "?"]
]

mina_lin = 2
mina_col = 2

jogando = True

while jogando:
    for linha in campo:
        print(*linha)

    lin = int(input("Linha (1–4): ")) - 1
    col = int(input("Coluna (1–4): ")) - 1

    if lin == mina_lin and col == mina_col:
        campo[lin][col] = "💥"
        print("BOOM! Você encontrou a mina!")
        jogando = False
    else:
        campo[lin][col] = "·"
        print("Seguro.")

print("Fim do jogo!")
for linha in campo:
    print(*linha)
