# ==================================================
# ESERCIZIO 8 - Tris
# ==================================================
# Gioco del tris utente vs utente

turno = 1
giocatore = 1
griglia = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

mosse = {
    1: (0,0),
    2: (0,1),
    3: (0,2),
    4: (1,0),
    5: (1,1),
    6: (1,2),
    7: (2,0),
    8: (2,1),
    9: (2,2),
}


def valore(val):
    if val == 0:
        return "_"
    elif val == 1:
        return "X"
    else:
        return "O"


def stampa_griglia():
    for riga in griglia:
        print(f"| {valore(riga[0])} | {valore(riga[1])} | {valore(riga[2])} |")


def inserisci_mossa(mossa):
    if griglia[mosse[mossa][0]][mosse[mossa][1]] == 0:
        griglia[mosse[mossa][0]][mosse[mossa][1]] = giocatore
        return True
    else:
        print("Mossa non consentita, casella già inserita")
        return False
    


def cambia_giocatore():
    global giocatore
    if giocatore == 1:
        giocatore = 2
    else:
        giocatore = 1


def incrementa_turno():
    global turno
    turno = turno + 1


def verifica_vittoria():

    #verifica vittoria righe
    if (griglia[0][0] == griglia[0][1] == griglia[0][2]) and griglia[0][0] != 0:
        return True
    
    if (griglia[1][0] == griglia[1][1] == griglia[2][2]) and griglia[1][0] != 0:
        return True
    
    if (griglia[2][0] == griglia[2][1] == griglia[2][2]) and griglia[2][0] != 0:
        return True
        
    # verifica vittoria colonne
    if (griglia[0][0] == griglia[1][0] == griglia[2][0]) and griglia[0][0] != 0:
        return True
    
    if griglia[0][1] == griglia[1][1] == griglia[2][1] and griglia[0][1] != 0:
        return True
    
    if griglia[0][2] == griglia[1][2] == griglia[2][2] and griglia[0][2] != 0:
        return True
    
    # verifica vittoria diagonali
    if griglia[0][0] == griglia[1][1] == griglia[2][2] and griglia[0][0] != 0:
        return True
    
    if griglia[0][2] == griglia[1][1] == griglia[2][0] and griglia[0][2] != 0:
        return True
    
    return False



while True:
    stampa_griglia()
    casella = int(input("Inserisci casella: "))

    if inserisci_mossa(casella):
        cambia_giocatore()
        incrementa_turno()

    if verifica_vittoria():
        print("Vittoria")
        break

    if turno > 9:
        break

stampa_griglia()