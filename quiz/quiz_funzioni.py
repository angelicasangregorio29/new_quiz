from quiz_domande import lista_domande, lista_domande_length

def mostra_domanda(indice):
    print(f"\nDomanda {indice+1} di {lista_domande_length}")
    print("------------------------------")
    print(lista_domande[indice]["testo"])

def salva_risultato(risultato_finale, indice, esito):
    if len(risultato_finale) > indice:
        risultato_finale[indice] = esito
        print(f"Risultato aggiornato per la domanda {indice+1}: {esito}")
    else:
        risultato_finale.append(esito)
        print(f"Risultato salvato per la domanda {indice+1}: {esito}")

def gestisci_navigazione(indice_corrente):
    scelta = input("Vuoi andare (P)recedente, (S)uccessiva o saltare a un numero? ").strip()

    if scelta.upper() == "P":
        if indice_corrente > 0:
            print("Vai alla domanda precedente.")
            return indice_corrente - 1
        else:
            print("Sei già alla prima domanda, non puoi tornare indietro.")
            return indice_corrente
    elif scelta.upper() == "S":
        if indice_corrente < lista_domande_length - 1:
            print("Vai alla domanda successiva.")
            return indice_corrente + 1
        else:
            print("Sei già all'ultima domanda, non puoi andare oltre.")
            return indice_corrente
    elif scelta.isdigit():
        numero = int(scelta)
        if 1 <= numero <= lista_domande_length:
            print(f"Salto alla domanda numero {numero}.")
            return numero - 1
        else:
            print("Numero non valido, rimaniamo sulla stessa domanda.")
            return indice_corrente
    else:
        print("Scelta non riconosciuta, passo alla domanda successiva.")
        return indice_corrente + 1