from typing import Any


class Atleta:

    nome = ""
    peso = 0
    altezza = 0
    IMC = 0.0
    mesiEsperienza = 0
    esperienza = ""
    livelloEsperienza = 120
    traguardo = ""
    categoria = ""
    messaggio = ""

    def __init__(self, nome, peso, altezza):
        self.nome = nome
        self.peso = peso
        self.altezza = altezza

    def printAtleta(self):
        return "Nome: " + self.nome + "\n" + "Peso (in kg): " + str(self.peso) + "\n" + "Altezza (in cm): " + str(self.altezza) + "\n" + "Indice Massa Corporea (IMC): " + str(self.IMC) + "\n" + "Mesi esperienza: " + str(self.mesiEsperienza) + "\n"\
            + "Esperienza: " + self.esperienza + "\n" + "Livello Esperienza: " + str(self.livelloEsperienza) + "\n" + "Traguardo: " + self.traguardo + "\n" + "Categoria: " + self.categoria + "\n" + "Messaggio: " + self.nome + self.messaggio





