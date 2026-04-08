# ==================================================
# ESEMPIO 3 - iterazioni: while e for
# ==================================================

# while
# while ripete un blocco di istruzioni finché una condizione è vera.
contatore = 1

while contatore <= 5:
    print("Conteggio:", contatore)
    contatore = contatore + 1


# while con input
# Il ciclo continua finché l'utente non inserisce 0.
numero = int(input("Inserisci un numero (0 per terminare): "))

while numero != 0:
    print("Hai inserito:", numero)
    numero = int(input("Inserisci un numero (0 per terminare): "))

print("Ciclo terminato.")



# for su una stringa
# Il ciclo for può scorrere i caratteri di una stringa.
parola = "Python"

for carattere in parola:
    print(carattere)


# for su una lista
# Il ciclo for può scorrere gli elementi di una lista.
numeri = [10, 20, 30, 40]

for numero in numeri:
    print("Elemento:", numero)


# for con indice ed elemento
# enumerate permette di ottenere sia la posizione sia il valore.
colori = ["rosso", "verde", "blu"]

for indice, colore in enumerate(colori):
    print("Posizione:", indice, "- Colore:", colore)



# for con range
# range permette di generare una sequenza di numeri.
for i in range(5):
    print("Valore di i:", i)


# for con range specificando inizio e fine
for i in range(1, 6):
    print("Numero:", i)


# for con passo
# Il terzo valore di range rappresenta il passo.
for i in range(0, 10, 2):
    print("Numero pari:", i)


# break
# break interrompe il ciclo.
for i in range(1, 11):
    if i == 6:
        break
    print(i)


# continue
# continue salta l'iterazione corrente e passa alla successiva.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)