class Jogo:
    nome = ""
    genero = ""
    jogadoes = 0

    def iniciar(self):
        print("iniciando", self.nome)

    def jogar(self):
        print("jogando", self.nome, "com", self.jogadoes, "jogadores")


j1 = Jogo()
j1.nome = "Minecraft"
j1.genero = "Sanbox"
j1.jogadoes = 30

print(f'Jogo: {j1.nome} - Genero: {j1.genero}')


j1.iniciar()
j1.jogar()

j2 = Jogo()
j2.nome = "Mario Wonder"
j2.genero = "Plataforma"
j2.jogadoes = 4

print("")
print("")

print(f'Jogo: {j2.nome} - Genero: {j2.genero}')

j2.iniciar()
j2.jogar()
