VUOTO = "_"
GIOCATORE_1 = "X"
GIOCATORE_2 = "O"

def stampa_scacchiera(scacchiera):
    for i in range(0, 9, 3):
        print(f"{scacchiera[i]} | {scacchiera[i+1]} | {scacchiera[i+2]}")


def fai_mossa(scacchiera, posizione, giocatore):

    # controllo che la posizione sia valida
    if posizione < 1 or posizione > 9:
        return False

    # posizione - 1 perché la lista parte da 0
    indice = posizione - 1

    # controllo che la casella sia libera
    if scacchiera[indice] == VUOTO:
        scacchiera[indice] = giocatore
        return True

    return False


def ha_vinto(scacchiera, giocatore):

    # controllo righe
    for i in range(0, 9, 3):
        if (
            scacchiera[i] == giocatore and
            scacchiera[i + 1] == giocatore and
            scacchiera[i + 2] == giocatore
        ):
            return True

    # controllo colonne
    for i in range(0, 3):
        if (
            scacchiera[i] == giocatore and
            scacchiera[i + 3] == giocatore and
            scacchiera[i + 6] == giocatore
        ):
            return True

    # diagonale principale
    if (
        scacchiera[0] == giocatore and
        scacchiera[4] == giocatore and
        scacchiera[8] == giocatore
    ):
        return True

    # diagonale secondaria
    if (
        scacchiera[2] == giocatore and
        scacchiera[4] == giocatore and
        scacchiera[6] == giocatore
    ):
        return True

    return False


def cambia_giocatore(giocatore):

    if giocatore == GIOCATORE_1:
        return GIOCATORE_2

    return GIOCATORE_1


def piena(scacchiera):

    if VUOTO not in scacchiera:
        return True

    return False


if __name__ == "__main__":

    scacchiera = [VUOTO] * 9
    corrente = GIOCATORE_1

    while True:

        stampa_scacchiera(scacchiera)

        try:
            posizione_mossa = int(
                input(f"\nInserisci mossa giocatore {corrente} (1-9): ")
            )

        except ValueError:
            print("Errore: inserire un numero valido")
            continue

        mossa_valida = fai_mossa(
            scacchiera,
            posizione_mossa,
            corrente
        )

        if not mossa_valida:
            print("Mossa non consentita, riprovare")
            continue

        if ha_vinto(scacchiera, corrente):

            stampa_scacchiera(scacchiera)

            print(f"\nVittoria giocatore {corrente}")

            break

        if piena(scacchiera):

            stampa_scacchiera(scacchiera)

            print("\nPareggio!")

            break

        corrente = cambia_giocatore(corrente)