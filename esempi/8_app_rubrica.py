# ==================================================
# ESEMPIO 7 - mini app rubrica
# In questo esempio è presente una piccola applicazione
# organizzata con più funzioni.
# I contatti vengono salvati in una lista di dizionari.
# ==================================================

# Dati
# La lista contatti contiene un dizionario per ogni contatto.
contatti = []


# Funzione aggiunta contatto
# Questa funzione legge i dati da tastiera e aggiunge un nuovo contatto.
def aggiungi_contatto():
    nome = input("Nome: ").strip()
    telefono = input("Telefono: ").strip()

    contatto = {
        "nome": nome,
        "telefono": telefono
    }

    contatti.append(contatto)
    print("Contatto aggiunto.")


# Funzione visualizzazione contatti
# Questa funzione mostra tutti i contatti presenti nella rubrica.
def visualizza_contatti():
    # Se la lista è vuota, non ci sono contatti da mostrare.
    if not contatti:
        print("Nessun contatto presente.")
        return

    # Ogni elemento della lista è un dizionario che rappresenta un contatto.
    for contatto in contatti:
        print(f"{contatto['nome']} - {contatto['telefono']}")


# Menu
# Il menu permette di ripetere più operazioni finché non si sceglie di uscire.
def menu():
    while True:
        print("\n--- RUBRICA ---")
        print("1. Aggiungi contatto")
        print("2. Visualizza contatti")
        print("0. Esci")

        scelta = input("Scelta: ").strip()

        if scelta == "1":
            aggiungi_contatto()
        elif scelta == "2":
            visualizza_contatti()
        elif scelta == "0":
            break
        else:
            print("Scelta non valida.")


# Avvio del programma
# Quando il file viene eseguito direttamente, viene chiamata la funzione menu().
if __name__ == "__main__":
    menu()