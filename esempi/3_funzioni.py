# ==================================================
# ESEMPIO 3 - funzioni
# ==================================================

# Funzione senza return
def saluta(nome):
    print(f"Ciao {nome}!")


# Funzione con return
def somma(a, b):
    risultato = a + b
    return risultato


# Funzione Main 
# L'interprete python esegue le righe contenute nel file una alla volta
# tuttavia è possibile creare una funzione main per questioni di chiarezza del file
def main():
    nome = input("Nome: ")
    saluta(nome)

    x = int(input("Primo numero: "))
    y = int(input("Secondo numero: "))
    risultato = somma(x, y)
    print(f"La somma è {risultato}.")


# La funzione main non viene eseguita a meno che non venga richiamata
if __name__ == "__main__":
    main()