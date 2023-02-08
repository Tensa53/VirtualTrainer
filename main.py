import os
import random

from deap.tools import HallOfFame

import atleta
import sys

from deap import base, algorithms
from deap import creator
from deap import tools

import constants
import eserciziPopulator

#Atleta di esempio:
#Nome: Gianni
#Peso: 70kg
#Altezza: 160cm
#Mesi Esperienza: 0

#conf di base
#select: tournament
#crossover: twoPoint
#mutation: UniFormInt

#sperimentare cambiando un parametro alla volta
#esperimento 1:
#select: truncation
#crossover: twoPoint
#mutation: UniFormInt
#esperimento 2:
#select: tournament
#crossover: onePoint
#mutation: UniFormInt
#esperimento 3:
#select: truncation
#crossover: onePoint
#mutation: UniFormInt


myAtleta = atleta.Atleta()
eserciziFactory = eserciziPopulator.eserciziPopulator(90)
eserciziFactory.populateEsercizi()

POPSIZE = 10
NUMEX = 6
MATPOOL = 4
FIRST = False
CXPB = 0.5
NGEN = 5
MTPB = 0.2
LOW = 0
UP = 89


def calcoloSfida(individual):
    sfidasum = 0
    avgsfidasum = 0

    for i in individual:
        myEsercizio = eserciziFactory.getEsercizioByID(i)
        sfida = constants.SFIDAMAX - abs(myAtleta.livelloEsperienza - myEsercizio.livellodifficolta)
        sfidasum += sfida

    avgsfidasum = sfidasum / len(individual)
    return avgsfidasum


def affinitaEsercizio(esercizio):
    val = 0

    if myAtleta.categoria == constants.CATEGORIA[0] and esercizio.tipologia == constants.TIPOLOGIA[0]:
        val = 100

    if myAtleta.categoria == constants.CATEGORIA[0] and esercizio.tipologia == constants.TIPOLOGIA[1]:
        val = 300

    if myAtleta.categoria == constants.CATEGORIA[1] and esercizio.tipologia == constants.TIPOLOGIA[0]:
        val = 200

    if myAtleta.categoria == constants.CATEGORIA[1] and esercizio.tipologia == constants.TIPOLOGIA[1]:
        val = 300

    if myAtleta.categoria == constants.CATEGORIA[2] and esercizio.tipologia == constants.TIPOLOGIA[0]:
        val = 300

    if myAtleta.categoria == constants.CATEGORIA[2] and esercizio.tipologia == constants.TIPOLOGIA[1]:
        val = 300

    if myAtleta.categoria == constants.CATEGORIA[3] and esercizio.tipologia == constants.TIPOLOGIA[0]:
        val = 300

    if myAtleta.categoria == constants.CATEGORIA[3] and esercizio.tipologia == constants.TIPOLOGIA[1]:
        val = 200

    if myAtleta.categoria == constants.CATEGORIA[4] and esercizio.tipologia == constants.TIPOLOGIA[0]:
        val = 300

    if myAtleta.categoria == constants.CATEGORIA[4] and esercizio.tipologia == constants.TIPOLOGIA[1]:
        val = 100

    return val


def calcoloAffinita(individual):
    affinitasum = 0
    avgaffintasum = 0

    for i in individual:
        fit = affinitaEsercizio(eserciziFactory.getEsercizioByID(i))
        affinitasum += fit

    avgaffintasum = affinitasum/len(individual)
    return avgaffintasum


def evaluateInd(individual):
    avgsfida = calcoloSfida(individual)
    avgaffinita = calcoloAffinita(individual)

    # print("Sfida scheda: " + str(avgsfida))
    # print("Affinita scheda: " + str(avgaffinita))
    #
    # input("Premere un tasto per continuare...")

    return avgaffinita, avgsfida


def configuraParametriAlgoritmo():
    creator.create("FitnessMulti", base.Fitness, weights=(1.0, 1.0))
    creator.create("Individual", list, fitness=creator.FitnessMulti)

    toolbox = base.Toolbox()
    toolbox.register("attr_int", random.randint, LOW, UP)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, n=NUMEX)

    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutUniformInt, low=LOW, up=UP, indpb=0.5)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", evaluateInd)

    return toolbox


def algoritmoSemplice(toolbox):
    pop = toolbox.population(n=POPSIZE)

    hof = tools.HallOfFame(4)

    print("Initial population:")
    for p in pop:
        print(str(p) + "" + str(p.fitness))

    print()

    for g in range(NGEN):
        print("GEN " + str(g))

        # SELEZIONE
        offspring = toolbox.select(pop, MATPOOL)

        # print("Post selection:")
        # for o in offspring:
        #     print(str(o) + "" + str(o.fitness))
        #
        # print()

        # CROSSOVER
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        # print("Post crossover:")
        # for o in offspring:
        #     print(str(o) + "" + str(o.fitness))
        #
        # print()

        # MUTAZIONE
        for mutant in offspring:
            if random.random() < MTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # print("Post mutation:")
        # for o in offspring:
        #     print(str(o) + "" + str(o.fitness))
        #
        # print()

        # VALUTAZIONE
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # MEMORIZZAZIONE DELLA NUOVA POPOLAZIONE
        pop[:] = offspring

        print("Post evaluation:")
        for p in pop:
            print(str(p) + "" + str(p.fitness))

        print()

        # MEMORIZZAZIONE DEL MIGLIOR INDIVIDUO
        hof.update(pop)

    for h in hof:
        print(str(h) + "" + str(h.fitness))

    print()

    print("Best Individual: " + str(hof[0]) + str(hof[0].fitness))

    input("Premi un tasto per continuare...")


def generaScheda():

    if FIRST:
        if myAtleta.isGraveMagrezzaorObeso():
            print("Il tuo attuale peso non ti permette di procedere con la generazione scheda")
            input("Premi un tasto per continuare...")
            return

        toolbox = configuraParametriAlgoritmo()
        scheda = algoritmoSemplice(toolbox)

    else:
        print("Per generare la scheda, inserisci prima le informazioni")
        input("Premi un tasto per continuare...")
        return


def inserisciInfoAtleta():
    nome = input("Inserisci il tuo nome: ")
    peso = int(input("Inserisci il tuo peso (in kg): "))
    altezza = int(input("Inserisci la tua altezza (in cm): "))
    mesiEsperienza = int(input("Inserisci i tuoi mesi di esperienza nel fitness: "))

    myAtleta.nome = nome
    myAtleta.peso = peso
    myAtleta.altezza = altezza
    myAtleta.mesiEsperienza = mesiEsperienza

    global FIRST
    FIRST = True


def modificaInfoAtleta(n):
    if n == 1:
        nome = input("Inserisci un nuovo nome: ")
        myAtleta.nome = nome
    if n == 2:
        peso = int(input("Inserisci il tuo nuovo peso (in kg): "))
        myAtleta.peso = peso
    if n == 3:
        altezza = int(input("Inserisci la tua nuova altezza (in cm): "))
        myAtleta.altezza = altezza
    if n == 4:
        mesiEsperienza = int(input("Inserisci i tuoi mesi di esperienza nel fitness: "))
        myAtleta.mesiEsperienza = mesiEsperienza


def testScheda():
    esercizi = [60, 54, 40, 71, 54, 65]

    evaluateInd(esercizi)


def menu():
    while True:
        os.system("clear")
        print("VIRTUAL TRAINER")
        print("0. Esci dal programma")
        print("1. Inserisci informazioni atleta")
        print("2. Modifica informazioni atleta")
        print("3. Mostra caratteristiche atleta")
        print("4. Genera una scheda esercizi")
        n = int(input())

        if n == 0:
            sys.exit(0)

        elif n == 1:
            inserisciInfoAtleta()
            myAtleta.calcolaCaratteristiche()

        elif n == 2:
            if FIRST:
                print(myAtleta.printAtletaInfoPrompt())
                n=int(input("Seleziona l'info da modificare: "))
                modificaInfoAtleta(n)
                myAtleta.calcolaCaratteristiche()
                print("Informazioni aggiornate. Le tue caratteristiche sono cambiate")
                input("Premi un tasto per continuare...")
            else:
                print("Devi prima inserire le informazioni")
                input("Premi un tasto per continuare...")

        elif n == 3:
            if FIRST:
                print(myAtleta.printAtletaFull())
                input("Premi un tasto per continuare...")
            else:
                print("Devi prima inserire le informazioni")
                input("Premi un tasto per continuare...")

        elif n == 4:
            generaScheda()

        else:
            print("Seleziona una voce valida")
            input("Premi un tasto per continuare...")


menu()

