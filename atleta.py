import constants
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

    def __init__(self):
        self.mesiEsperienza = 120

    def areFeaturesEmpty(self):
        val = bool(self.IMC == 0) and bool(self.livelloEsperienza == 120) and bool(self.esperienza == "") and bool(self.traguardo == "") and  bool(self.messaggio == "") and  bool(self.categoria == "")
        print(val)
        return val

    def mostraCaratteristiche(self):
        val = bool(self.areFeaturesEmpty())

        if val:
            self.calcolaCaratteristiche()

        print(self.printAtleta())

    def calcolaCaratteristiche(self):
        self.calcolaIMC()

        self.calcolaLivelloEsperienza()

        self.calcolaTraguardo()

    def calcolaIMC(self):
        altezza100 = self.altezza / 100.0

        altezza2 = altezza100 * altezza100

        IMC = self.peso / altezza2

        self.IMC = IMC

    def calcolaLivelloEsperienza(self):
        livelloEsperienza = self.mesiEsperienza * 10
        self.livelloEsperienza = livelloEsperienza

        if livelloEsperienza <= 360:
            self.esperienza = constants.ESPERIENZA[0]

        if livelloEsperienza >= 370 and livelloEsperienza <= 600:
            self.esperienza = constants.ESPERIENZA[1]

        if livelloEsperienza >= 610 and livelloEsperienza <= 840:
            self.esperienza = constants.ESPERIENZA[2]

        if livelloEsperienza >= 850:
            self.esperienza = constants.ESPERIENZA[3]
            self.livelloEsperienza = 850

    def calcolaTraguardo(self):
        if self.IMC < 16:
            self.categoria = constants.CATEGORIA[5]
            self.traguardo = constants.TRAGUARDO[3]
            self.messaggio = constants.MESSAGGIO[5]

        if 16.0 <= self.IMC < 19.0:
            self.categoria = constants.CATEGORIA[0]
            self.traguardo = constants.TRAGUARDO[0]
            self.messaggio = constants.MESSAGGIO[0]

        if 19.0 <= self.IMC < 20.0:
            self.categoria = constants.CATEGORIA[1]
            self.traguardo = constants.TRAGUARDO[0]
            self.messaggio = constants.MESSAGGIO[1]

        if 20.0 <= self.IMC < 24.0:
            self.categoria = constants.CATEGORIA[2]
            self.traguardo = constants.TRAGUARDO[1]
            self.messaggio = constants.MESSAGGIO[2]

        if 24.0 <= self.IMC <= 25:
            self.categoria = constants.CATEGORIA[3]
            self.traguardo = constants.TRAGUARDO[2]
            self.messaggio = constants.MESSAGGIO[3]

        if 25 < self.IMC < 30:
            self.categoria = constants.CATEGORIA[4]
            self.traguardo = constants.TRAGUARDO[2]
            self.messaggio = constants.MESSAGGIO[4]

        if self.IMC > 30:
            self.categoria = constants.CATEGORIA[6]
            self.traguardo = constants.TRAGUARDO[3]
            self.messaggio = constants.MESSAGGIO[6]

    def isGraveMagrezzaorObeso(self):
        val1 = bool(self.categoria == constants.CATEGORIA[5])
        val2 = bool(self.categoria == constants.CATEGORIA[6])

        val3 = val1 or val2

        return val3

    def printAtleta(self):
        return "Nome: " + self.nome + "\n" + "Peso (in kg): " + str(self.peso) + "\n" + "Altezza (in cm): " + str(self.altezza) + "\n" + "Indice Massa Corporea (IMC): " + str(self.IMC) + "\n" + "Mesi esperienza: " + str(self.mesiEsperienza) + "\n"\
            + "Esperienza: " + self.esperienza + "\n" + "Livello Esperienza: " + str(self.livelloEsperienza) + "\n" + "Traguardo: " + self.traguardo + "\n" + "Categoria: " + self.categoria + "\n" + "Messaggio: " + self.nome + self.messaggio





