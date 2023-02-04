import random

import constants
import esercizio

class eserciziPopulator:

    numeroEsercizi = 0

    esercizio0 = esercizio.Esercizio("esercizio0", constants.PARTEDELCORPO[0], constants.DIFFICOLTA[0], constants.LIVELLODIFFICOLTA[0], constants.TIPOLOGIA[1])

    eserciziList = [esercizio0]

    def __init__(self, numeroEsercizi):
        self.numeroEsercizi = numeroEsercizi

    def populateEsercizi(self):
        for i in range(1, self.numeroEsercizi):
            nome = "esercizio"+str(i)

            ind1 = random.randint(0, 5)
            ind2 = random.randint(0,1)
            ind3 = random.randint(0,2)
            ind4 = random.randint(0,1)

            parteDelCorpo = constants.PARTEDELCORPO[ind1]
            difficolta = constants.DIFFICOLTA[ind2]
            livelloDifficolta = constants.LIVELLODIFFICOLTA[ind3]
            tipologia = constants.TIPOLOGIA[ind4]

            ex = esercizio.Esercizio(nome,parteDelCorpo,difficolta,livelloDifficolta,tipologia)

            self.eserciziList.append(ex)


    def getEsercizioByID(self, id):
        return self.eserciziList[id]


