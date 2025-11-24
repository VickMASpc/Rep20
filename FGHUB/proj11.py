def checar_numero(numero):
    if numero > 0:
        print(f"O número {numero} é positivo.")
    elif numero < 0:
        print(f"O número {numero} é negativo.")
    else:
        print(f"O número {numero} é zero.")


num = int(input("Digite o número: "))

checar_numero(num)
