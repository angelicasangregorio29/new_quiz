from quiz_domande import lista_domande, lista_domande_length
from quiz_funzioni import mostra_domanda, salva_risultato, gestisci_navigazione
from quiz_utils import mostra_istruzioni, calcola_punteggio

risultato_finale = []

def avvia_quiz():
    counter_domanda_corrente = 0
    while counter_domanda_corrente < lista_domande_length:
        mostra_domanda(counter_domanda_corrente)
        risposta_utente = input("Risposta: ").lower()

        if risposta_utente == lista_domande[counter_domanda_corrente]["risposta"]:
            print("Hai indovinato!")
            esito = True
        else:
            print("Non hai indovinato.")
            esito = False

        salva_risultato(risultato_finale, counter_domanda_corrente, esito)
        counter_domanda_corrente = gestisci_navigazione(counter_domanda_corrente)

    punteggio = calcola_punteggio(risultato_finale)
    print("\n✅ Quiz terminato!")
    print("Risultati finali:", risultato_finale)
    print(f"Hai totalizzato {punteggio}/{lista_domande_length} risposte corrette.")

def menu():
    while True:
        print("\n=== MENU PRINCIPALE ===")
        print("1. Inizia Quiz")
        print("2. Istruzioni")
        print("3. Esci")

        scelta = input("Seleziona un'opzione (1-3): ").strip()

        if scelta == "1":
            avvia_quiz()
        elif scelta == "2":
            mostra_istruzioni()
        elif scelta == "3":
            print("👋 Uscita dal programma. A presto!")
            break
        else:
            print("Opzione non valida, riprova.")

# Avvio del programma
if __name__ == "__main__":
    menu()