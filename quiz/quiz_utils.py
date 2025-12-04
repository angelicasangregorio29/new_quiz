def mostra_istruzioni():
    print("\n📖 Istruzioni del Quiz:")
    print("1. Ti verrà mostrata una domanda alla volta.")
    print("2. Dopo aver risposto, puoi scegliere:")
    print("   - 'P' per tornare alla domanda precedente")
    print("   - 'S' per andare alla successiva")
    print("   - Un numero (es. '3') per saltare direttamente a quella domanda")
    print("3. Alla fine vedrai i tuoi risultati complessivi.\n")

def calcola_punteggio(risultato_finale):
    return sum(risultato_finale)