# ==================================================
# ESEMPIO 5 - dizionari
# ==================================================


# Un dizionario è una struttura dati che associa una chiave a un valore.
studente = {
    "nome": "Luca",
    "eta": 17,
    "classe": "3A"
}
print(studente)

# Accesso tramite chiave
# Nei dizionari non si usano gli indici, ma le chiavi.
print(studente["nome"])
print(studente["eta"])


# Modifica di un valore
studente["eta"] = 18


# Aggiunta di una nuova coppia chiave-valore
studente["citta"] = "Imola"


# Lettura di un valore dopo la modifica
print(studente["eta"])
print(studente["citta"])


# Lunghezza di un dizionario
# len() restituisce il numero di coppie chiave-valore presenti nel dizionario.
print(len(studente))