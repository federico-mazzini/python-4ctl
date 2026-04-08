# ==================================================
# ESEMPIO 4 - liste
# ==================================================

# Creazione

# Una lista è una struttura dati che può contenere più valori (come un array in c++)
numeri = [10, 20, 30]
print(numeri)

# Una lista può contenere anche stringhe.
nomi = ["Luca", "Anna", "Marco"]
print(nomi)

# Gli elementi sono acceduti tramite indice
print(numeri[0]) # Il primo elemento si trova in posizione 0.
print(numeri[1]) # Secondo elemento


# Modifica di un elemento
numeri[1] = 25


# Aggiunta in coda
numeri.append(40) # append() aggiunge un nuovo elemento alla fine della lista.


# Lunghezza di una lista
print(len(numeri)) # len() restituisce il numero di elementi presenti nella lista.