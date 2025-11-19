class Carro:
    marca = ""
    modelo = ""
    ano = 0
    cor = ""

    def buzinar(self):
        print("Bi-Bi")

    def ligar(self):
        print("O carro ligou...")

    def acelerar(self):
        print("O carro acelerou")

    def freiar(self):
        print("O carro freiou")

    def desligar(self):
        print("O carro desligou...")


c1 = Carro()
c1.marca = "Nissan"
c1.modelo = "Nissan GT3"
c1.ano = 2006
c1.cor = "Azul"

print("Carro:", c1.marca, "-", c1.modelo,
      "Ano:", c1.ano, "Cor:", c1.cor)
c1.ligar()
c1.acelerar()
c1.buzinar()
c1.freiar()
c1.desligar()
