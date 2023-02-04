import random
import atleta
import sys

from deap import base
from deap import creator
from deap import tools

import eserciziPopulator

myAtleta = atleta.Atleta()



def inserisciInfoAtleta():
    nome = input("Inserisci il tuo nome: ")
    peso = int(input("Inserisci il tuo peso (in kg): "))
    altezza = int(input("Inserisci la tua altezza (in cm): "))
    mesiEsperienza = int(input("Inserisci i tuoi mesi di esperienza nel fitness: "))

    myAtleta.nome = nome
    myAtleta.peso = peso
    myAtleta.altezza = altezza
    myAtleta.mesiEsperienza = mesiEsperienza


def menu():
    while True:
        print("VIRTUAL TRAINER")
        print("0. Esci")
        print("1. Inserisci informazioni atleta")
        print("2. Mostra caratteristiche atleta")
        print("3. Genera una scheda esercizi")
        n = int(input())

        if n == 0:
            sys.exit(0)

        if n == 1:
            inserisciInfoAtleta()

        if n == 2:
            myAtleta.mostraCaratteristiche()

        if n == 3:
            print("TODO")


menu()

