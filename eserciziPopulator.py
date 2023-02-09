import random

import constants
import esercizio

class eserciziPopulator:

    numeroEsercizi = 0
    eserciziList = []

    def __init__(self, numeroEsercizi):
        self.numeroEsercizi = numeroEsercizi

    def populateEsercizi(self):
        #9 per ogni parte del corpo, 3 per ogni difficolta, totale 45 esercizi anaerobici
        #15 esercizi aerobici per ogni difficolta, totale 45 esercizi aerobici
        #in tutto abbiamo 90 esercizi

        esercizio0 = esercizio.Esercizio("esercizio0", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                         constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio1 = esercizio.Esercizio("esercizio1", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                         constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio2 = esercizio.Esercizio("esercizio2", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                         constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio3 = esercizio.Esercizio("esercizio3", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                         constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio4 = esercizio.Esercizio("esercizio4", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                         constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio5 = esercizio.Esercizio("esercizio5", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                         constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio6 = esercizio.Esercizio("esercizio6", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                         constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])
        esercizio7 = esercizio.Esercizio("esercizio7", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                         constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])
        esercizio8 = esercizio.Esercizio("esercizio8", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                         constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])

        esercizio9 = esercizio.Esercizio("esercizio9", constants.PARTEDELCORPO[1], constants.DIFFICOLTA[0],
                                         constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio10 = esercizio.Esercizio("esercizio10", constants.PARTEDELCORPO[1], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio11 = esercizio.Esercizio("esercizio11", constants.PARTEDELCORPO[1], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio12 = esercizio.Esercizio("esercizio12", constants.PARTEDELCORPO[1], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio13 = esercizio.Esercizio("esercizio13", constants.PARTEDELCORPO[1], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio14 = esercizio.Esercizio("esercizio14", constants.PARTEDELCORPO[1], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio15 = esercizio.Esercizio("esercizio15", constants.PARTEDELCORPO[1], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])
        esercizio16 = esercizio.Esercizio("esercizio16", constants.PARTEDELCORPO[1], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])
        esercizio17 = esercizio.Esercizio("esercizio17", constants.PARTEDELCORPO[1], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])

        esercizio18 = esercizio.Esercizio("esercizio18", constants.PARTEDELCORPO[2], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio19 = esercizio.Esercizio("esercizio19", constants.PARTEDELCORPO[2], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio20 = esercizio.Esercizio("esercizio20", constants.PARTEDELCORPO[2], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio21 = esercizio.Esercizio("esercizio21", constants.PARTEDELCORPO[2], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio22 = esercizio.Esercizio("esercizio22", constants.PARTEDELCORPO[2], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio23 = esercizio.Esercizio("esercizio23", constants.PARTEDELCORPO[2], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio24 = esercizio.Esercizio("esercizio24", constants.PARTEDELCORPO[2], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])
        esercizio25 = esercizio.Esercizio("esercizio25", constants.PARTEDELCORPO[2], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])
        esercizio26 = esercizio.Esercizio("esercizio26", constants.PARTEDELCORPO[2], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])

        esercizio27 = esercizio.Esercizio("esercizio27", constants.PARTEDELCORPO[3], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio28 = esercizio.Esercizio("esercizio28", constants.PARTEDELCORPO[3], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio29 = esercizio.Esercizio("esercizio29", constants.PARTEDELCORPO[3], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio30 = esercizio.Esercizio("esercizio30", constants.PARTEDELCORPO[3], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio31 = esercizio.Esercizio("esercizio31", constants.PARTEDELCORPO[3], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio32 = esercizio.Esercizio("esercizio32", constants.PARTEDELCORPO[3], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio33 = esercizio.Esercizio("esercizio33", constants.PARTEDELCORPO[3], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])
        esercizio34 = esercizio.Esercizio("esercizio34", constants.PARTEDELCORPO[3], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])
        esercizio35 = esercizio.Esercizio("esercizio35", constants.PARTEDELCORPO[3], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])

        esercizio36 = esercizio.Esercizio("esercizio36", constants.PARTEDELCORPO[4], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio37 = esercizio.Esercizio("esercizio37", constants.PARTEDELCORPO[4], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio38 = esercizio.Esercizio("esercizio38", constants.PARTEDELCORPO[4], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])
        esercizio39 = esercizio.Esercizio("esercizio39", constants.PARTEDELCORPO[4], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio40 = esercizio.Esercizio("esercizio40", constants.PARTEDELCORPO[4], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio41 = esercizio.Esercizio("esercizio41", constants.PARTEDELCORPO[4], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[1])
        esercizio42 = esercizio.Esercizio("esercizio42", constants.PARTEDELCORPO[4], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])
        esercizio43 = esercizio.Esercizio("esercizio43", constants.PARTEDELCORPO[4], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])
        esercizio44 = esercizio.Esercizio("esercizio44", constants.PARTEDELCORPO[4], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[1])

        esercizio45 = esercizio.Esercizio("esercizio45", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio46 = esercizio.Esercizio("esercizio46", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio47 = esercizio.Esercizio("esercizio47", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio48 = esercizio.Esercizio("esercizio48", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio49 = esercizio.Esercizio("esercizio49", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio50 = esercizio.Esercizio("esercizio50", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio51 = esercizio.Esercizio("esercizio51", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio52 = esercizio.Esercizio("esercizio52", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio53 = esercizio.Esercizio("esercizio53", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio54 = esercizio.Esercizio("esercizio54", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio55 = esercizio.Esercizio("esercizio55", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio56 = esercizio.Esercizio("esercizio56", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio57 = esercizio.Esercizio("esercizio57", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio58 = esercizio.Esercizio("esercizio58", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])
        esercizio59 = esercizio.Esercizio("esercizio59", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0],
                                          constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[0])

        esercizio60 = esercizio.Esercizio("esercizio60", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio61 = esercizio.Esercizio("esercizio61", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio62 = esercizio.Esercizio("esercizio62", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio63 = esercizio.Esercizio("esercizio63", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio64 = esercizio.Esercizio("esercizio64", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio65 = esercizio.Esercizio("esercizio65", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio66 = esercizio.Esercizio("esercizio66", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio67 = esercizio.Esercizio("esercizio67", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio68 = esercizio.Esercizio("esercizio68", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio69 = esercizio.Esercizio("esercizio69", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio70 = esercizio.Esercizio("esercizio70", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio71 = esercizio.Esercizio("esercizio71", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio72 = esercizio.Esercizio("esercizio72", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio73 = esercizio.Esercizio("esercizio73", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])
        esercizio74 = esercizio.Esercizio("esercizio74", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[1],
                                          constants.LIVELLODIFFICOLTA[1], constants.TIPOLOGIA[0])

        esercizio75 = esercizio.Esercizio("esercizio75", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio76 = esercizio.Esercizio("esercizio76", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio77 = esercizio.Esercizio("esercizio77", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio78 = esercizio.Esercizio("esercizio78", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio79 = esercizio.Esercizio("esercizio79", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio80 = esercizio.Esercizio("esercizio80", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio81 = esercizio.Esercizio("esercizio81", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio82 = esercizio.Esercizio("esercizio82", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio83 = esercizio.Esercizio("esercizio83", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio84 = esercizio.Esercizio("esercizio84", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio85 = esercizio.Esercizio("esercizio85", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio86 = esercizio.Esercizio("esercizio86", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio87 = esercizio.Esercizio("esercizio87", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio88 = esercizio.Esercizio("esercizio88", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])
        esercizio89 = esercizio.Esercizio("esercizio89", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[2],
                                          constants.LIVELLODIFFICOLTA[2], constants.TIPOLOGIA[0])

        self.eserciziList.append(esercizio0)
        self.eserciziList.append(esercizio1)
        self.eserciziList.append(esercizio2)
        self.eserciziList.append(esercizio3)
        self.eserciziList.append(esercizio4)
        self.eserciziList.append(esercizio5)
        self.eserciziList.append(esercizio6)
        self.eserciziList.append(esercizio7)
        self.eserciziList.append(esercizio8)
        self.eserciziList.append(esercizio9)

        self.eserciziList.append(esercizio10)
        self.eserciziList.append(esercizio11)
        self.eserciziList.append(esercizio12)
        self.eserciziList.append(esercizio13)
        self.eserciziList.append(esercizio14)
        self.eserciziList.append(esercizio15)
        self.eserciziList.append(esercizio16)
        self.eserciziList.append(esercizio17)
        self.eserciziList.append(esercizio18)
        self.eserciziList.append(esercizio19)
        self.eserciziList.append(esercizio20)

        self.eserciziList.append(esercizio21)
        self.eserciziList.append(esercizio22)
        self.eserciziList.append(esercizio23)
        self.eserciziList.append(esercizio24)
        self.eserciziList.append(esercizio25)
        self.eserciziList.append(esercizio26)
        self.eserciziList.append(esercizio27)
        self.eserciziList.append(esercizio28)
        self.eserciziList.append(esercizio29)
        self.eserciziList.append(esercizio30)

        self.eserciziList.append(esercizio31)
        self.eserciziList.append(esercizio32)
        self.eserciziList.append(esercizio33)
        self.eserciziList.append(esercizio34)
        self.eserciziList.append(esercizio35)
        self.eserciziList.append(esercizio36)
        self.eserciziList.append(esercizio37)
        self.eserciziList.append(esercizio38)
        self.eserciziList.append(esercizio39)
        self.eserciziList.append(esercizio40)

        self.eserciziList.append(esercizio41)
        self.eserciziList.append(esercizio42)
        self.eserciziList.append(esercizio43)
        self.eserciziList.append(esercizio44)
        self.eserciziList.append(esercizio45)
        self.eserciziList.append(esercizio46)
        self.eserciziList.append(esercizio47)
        self.eserciziList.append(esercizio48)
        self.eserciziList.append(esercizio49)
        self.eserciziList.append(esercizio50)

        self.eserciziList.append(esercizio51)
        self.eserciziList.append(esercizio52)
        self.eserciziList.append(esercizio53)
        self.eserciziList.append(esercizio54)
        self.eserciziList.append(esercizio55)
        self.eserciziList.append(esercizio56)
        self.eserciziList.append(esercizio57)
        self.eserciziList.append(esercizio58)
        self.eserciziList.append(esercizio59)
        self.eserciziList.append(esercizio60)

        self.eserciziList.append(esercizio61)
        self.eserciziList.append(esercizio62)
        self.eserciziList.append(esercizio63)
        self.eserciziList.append(esercizio64)
        self.eserciziList.append(esercizio65)
        self.eserciziList.append(esercizio66)
        self.eserciziList.append(esercizio67)
        self.eserciziList.append(esercizio68)
        self.eserciziList.append(esercizio69)
        self.eserciziList.append(esercizio70)

        self.eserciziList.append(esercizio71)
        self.eserciziList.append(esercizio72)
        self.eserciziList.append(esercizio73)
        self.eserciziList.append(esercizio74)
        self.eserciziList.append(esercizio75)
        self.eserciziList.append(esercizio76)
        self.eserciziList.append(esercizio77)
        self.eserciziList.append(esercizio78)
        self.eserciziList.append(esercizio79)
        self.eserciziList.append(esercizio80)

        self.eserciziList.append(esercizio81)
        self.eserciziList.append(esercizio82)
        self.eserciziList.append(esercizio83)
        self.eserciziList.append(esercizio84)
        self.eserciziList.append(esercizio85)
        self.eserciziList.append(esercizio86)
        self.eserciziList.append(esercizio87)
        self.eserciziList.append(esercizio88)
        self.eserciziList.append(esercizio89)

    def populateEserciziRandom(self):
        for i in range(0, self.numeroEsercizi):
            nome = "esercizio"+str(i)

            ind1 = random.randint(0, 5)
            ind2 = random.randint(0, 2)
            ind3 = random.randint(0, 2)
            ind4 = random.randint(0, 1)

            parteDelCorpo = constants.PARTEDELCORPO[ind1]
            difficolta = constants.DIFFICOLTA[ind2]
            livelloDifficolta = constants.LIVELLODIFFICOLTA[ind3]
            tipologia = constants.TIPOLOGIA[ind4]

            ex = esercizio.Esercizio(nome, parteDelCorpo, difficolta, livelloDifficolta, tipologia)

            self.eserciziList.append(ex)

    def getEsercizioByID(self, id):
        return self.eserciziList[id]


