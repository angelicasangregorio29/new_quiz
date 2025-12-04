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

 # --- Livello 3: Gestione della Memoria ---
    if len(risultato_finale) > counter_domanda_corrente:
        # Sovrascrivi la risposta già data
        risultato_finale[counter_domanda_corrente] = esito
    else:
        # Aggiungi nuova risposta
        risultato_finale.append(esito)

    # --- Livello 2 + Bonus: Navigazione ---
    scelta = input("Vuoi andare (P)recedente, (S)uccessiva o saltare a un numero? ").strip()

    if scelta.upper() == "P":
        if counter_domanda_corrente > 0:
            counter_domanda_corrente -= 1
        else:
            print("Sei già alla prima domanda, non puoi tornare indietro.")
    elif scelta.isdigit():
        numero = int(scelta)
        if 1 <= numero <= lista_domande_length:
            counter_domanda_corrente = numero - 1
        else:
            print("Numero non valido, rimaniamo sulla stessa domanda.")
    else:
        counter_domanda_corrente += 1

print("\nQuiz terminato!")
print("Risultati finali:", risultato_finale)

