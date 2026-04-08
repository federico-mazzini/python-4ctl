# ==================================================
# ESEMPIO 2 - if, else, elif, match
# ==================================================

# if else 
eta = int(input("Inserisci la tua età: "))

if eta >= 18:
    print("Sei maggiorenne.")
else:
    print("Sei minorenne.")


# elif
# elif permette di controllare casi diversi in sequenza.
voto = int(input("Inserisci un voto da 1 a 10: "))

if voto < 6:
    print("Il voto non è sufficiente.")
elif voto == 6:
    print("Il voto è sufficiente.")
else:
    print("Il voto è superiore alla sufficienza.")



# match
# match permette di scegliere tra casi diversi in base al valore di un'espressione.
# È simile allo switch visto in C++

giorno = int(input("Inserisci un numero da 1 a 7: "))

match giorno:
    case 1:
        print("Lunedi")
    case 2:
        print("Martedi")
    case 3:
        print("Mercoledi")
    case 4:
        print("Giovedi")
    case 5:
        print("Venerdi")
    case 6:
        print("Sabato")
    case 7:
        print("Domenica")
    case _:
        print("Errore")
