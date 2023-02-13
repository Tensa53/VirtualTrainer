# VirtualTrainer

## Partecipanti 
- Daniele Fabiano 
- Mariantonietta Maselli

## Che cos'è Virtual Trainer

Virtual Trainer nasce dall’idea di integrare un modulo intelligente all’interno
di un software ben più grande che è quello di SmartGym. SmartGym è
il nome del nostro progetto di Ingegneria del Software, il suo obiettivo è
quello di dematerializzare e digitalizzare il processo di creazione di una scheda
esercizi per la palestra. Virtual Trainer ricopre la funzionalità di generazione
di una scheda esercizi. Per questioni logistiche non è stato possibile integrare
i due sistemi. L’attuale implementazione è una versione semplificata dell’algoritmo 
che non tiene conto dei vincoli relativi all’interattività con l’utente. 
L’utente interagirà con l’algoritmo esclusivamente per inserire le sue informazioni.
La tecnica di risoluzione scelta prevede l'utilizzo di un algoritmo genetico.

## Come utilizzare il nostro algoritmo

Per utilizzare l'attuale implementazione sono necessari:
- Pycharm Community 2022.3
- Python 3.10
- Pip
- DEAP Framework 1.3.3

Per installare il framework DEAP è necessario lanciare il seguente comando:
``pip install deap``

Basterà quindi clonare il progetto per utilizzarlo attraverso l'IDE precedentemente citato
