# quiz_domande.py
# File contenente domande e risposte per un quiz a scelta multipla

quiz_domande = [
    {
        "domanda": "Qual è il linguaggio usato principalmente per lo sviluppo web lato client?",
        "opzioni": ["Python", "JavaScript", "C++", "Java"],
        "corretta": "JavaScript"
    },
    {
        "domanda": "Chi ha inventato il World Wide Web?",
        "opzioni": ["Bill Gates", "Tim Berners-Lee", "Steve Jobs", "Linus Torvalds"],
        "corretta": "Tim Berners-Lee"
    },
    {
        "domanda": "Quale colore si ottiene mescolando giallo e blu?",
        "opzioni": ["Rosso", "Verde", "Arancione", "Viola"],
        "corretta": "Verde"
    },
    {
        "domanda": "In Python, quale funzione serve per stampare a schermo?",
        "opzioni": ["echo()", "print()", "console.log()", "print()"],
        "corretta": "print()"
    },
    {
        "domanda": "Qual è la capitale d’Italia?",
        "opzioni": ["Milano", "Torino", "Roma", "Napoli"],
        "corretta": "Roma"
    }
]

def mostra_quiz():
    """Stampa tutte le domande del quiz con le opzioni."""
    for i, q in enumerate(quiz_domande, start=1):
        print(f"Domanda {i}: {q['domanda']}")
        for j, opzione in enumerate(q["opzioni"], start=1):
            print(f"   {j}. {opzione}")
        print()

def esegui_quiz():
    """Permette all'utente di rispondere e mostra il punteggio finale."""
    punteggio = 0
    for i, q in enumerate(quiz_domande, start=1):
        print(f"Domanda {i}: {q['domanda']}")
        for j, opzione in enumerate(q["opzioni"], start=1):
            print(f"   {j}. {opzione}")
        risposta = input("La tua risposta (numero): ")
        try:
            risposta_int = int(risposta)
            scelta = q["opzioni"][risposta_int - 1]
            if scelta == q["corretta"]:
                print("✅ Corretto!\n")
                punteggio += 1
            else:
                print(f"❌ Sbagliato! La risposta giusta era: {q['corretta']}\n")
        except (ValueError, IndexError):
            print("⚠️ Risposta non valida.\n")
    print(f"Hai totalizzato {punteggio} punti su {len(quiz_domande)}.")

if __name__ == "__main__":
    print("Benvenuto al quiz!\n")
    esegui_quiz()