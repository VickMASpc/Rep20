op = ""

while op != "4":
    print("1 - Olá")
    print("2 - Contar até 5")
    print("3 - Mostrar X 5 vezes")
    print("4 - Sair")

    op = input("Escolha: ")

    if op == "1":
        print("Olá usuário!")
    elif op == "2":
        for i in range(1, 6):
            print(i)
    elif op == "3":
        for x in range(5):
            print("X")
    elif op == "4":
        print("Saindo...")
    else:
        print("Opção inválida!")
