VUOTO = "_"
GIOCATORE_1 = "X"
GIOCATORE_2 = "O"

def stampa_scacchiera(scacchiera):
    for i in range(0, 8, 3):
        print (f"{scacchiera[i]} | {scacchiera[i+1]} | {scacchiera[i+2]}")

def fai_mossa(scacchiera, posizione, giocatore):
    # posizione - 1 perchè voglio che si giochi da 1 a 9 (più intuituivo per i giocatori)
    if(scacchiera[posizione - 1] == VUOTO):
        scacchiera[posizione - 1] = giocatore
        return True
    else:
        return False
    
def ha_vinto(scacchiera, giocatore):
    # righe
    for i in range(0,8,3):
        if(scacchiera[i] == giocatore and scacchiera[i+1] == giocatore and scacchiera[i+2] == giocatore):
            return True
        
    # colonne
    for i in range (0,2):
        if(scacchiera[i] == giocatore and scacchiera[i+3] == giocatore and scacchiera[i+6] == giocatore):
            return True
        
    #diagonale
    if(scacchiera[0] == giocatore and scacchiera[4] == giocatore and scacchiera[8] == giocatore):
        return True
    
    if(scacchiera[2] == giocatore and scacchiera[4] == giocatore and scacchiera[6] == giocatore):
        return True
    
    return False


def cambia_giocatore(giocatore):
    if(giocatore == GIOCATORE_1):
        return GIOCATORE_2
    else:
        return GIOCATORE_1

def piena(scacchiera):
    if VUOTO not in scacchiera:
        return True
    
    return False

if __name__ == "__main__":
    corrente = GIOCATORE_1
    scacchiera = [VUOTO] * 9

    while True:
        stampa_scacchiera(scacchiera)

        try:
            posizione_mossa = int(input(f"Inserire mossa giocatore {corrente}: "))
            mossa = fai_mossa(scacchiera, posizione_mossa, corrente)
        except:
            print("Errore nell'inserimento mossa, riprovare")
            continue

        if not mossa:
            print("Mossa non consentita, riprovare")
            continue
        
        if ha_vinto(scacchiera, corrente):
            print(f"Vittoria giocatore {corrente}")
            stampa_scacchiera(scacchiera)
            break

        if piena(scacchiera):
            print("Pareggio!")
            stampa_scacchiera(scacchiera)
            break

        corrente = cambia_giocatore(corrente)