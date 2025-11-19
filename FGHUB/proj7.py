comidasSaudaveis = [
    "uvas",
    "tomate",
    "nozes",
    "arroz",
    "cenoura",
    "lentilha",
    "frango",
    "peixe",
    "brócolis"
]

comidasNaoSaudaveis = [
    "salsicha",
    "mac'n cheese",
    "hamburgeres",
    "balas",
    "sorvete"
]

comidainput = input("Digite uma comida: ")

index = comidainput

if comidainput in comidasSaudaveis:
    print(f"Sim, {comidasSaudaveis[index]} esta comida é saudável.")
elif comidainput in comidasNaoSaudaveis:
    print("Não, esta comida não é saudável.")
else:
    print("Não conheço esta comida.")
