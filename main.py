# Lista di domande e risposte
lista_domande = [
    {"testo": "Qual è la capitale della Francia?", "risposta": "parigi"},
    {"testo": "Qual è la capitale dell'Italia?", "risposta": "roma"},
    {"testo": "Qual è la capitale della Spagna?", "risposta": "madrid"},
    {"testo": "Qual è la capitale della Germania?", "risposta": "berlino"},
    {"testo": "Qual è la capitale del Portogallo?", "risposta": "lisbona"}
]

lista_domande_length = len(lista_domande)
counter_domanda_corrente = 0
risultato_finale = []  # lista delle risposte date

def mostra_domanda(indice):
    print(f"Domanda {indice+1} di {lista_domande_length}")
    print("------------------------------")
    print(lista_domande[indice]["testo"])

while counter_domanda_corrente < lista_domande_length:
    mostra_domanda(counter_domanda_corrente)
    risposta_utente = input("Risposta: ").lower()

    # Feedback
    if risposta_utente == lista_domande[counter_domanda_corrente]["risposta"]:
        print("Hai indovinato!")
        esito = True
    else:
        print("Non hai indovinato.")
        esito = False

