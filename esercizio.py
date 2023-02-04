class Esercizio:

    nome = ""
    parteDelCorpo = ""
    difficolta = ""
    livellodifficolta = ""
    tipologia = ""

    def __init__(self, nome, parteDelCorpo, difficolta, livellodifficolta, tipologia):
        self.nome = nome
        self.parteDelCorpo = parteDelCorpo
        self.difficolta = difficolta
        self.livellodifficolta = livellodifficolta
        self.tipologia = tipologia

    def printEsercizio(self):
        return "Nome: " + self.nome + "\n" + "Parte del Corpo: " + self.parteDelCorpo + "\n" + "Difficolta: " + self.difficolta + "\n" + "Tipologia: " + self.tipologia