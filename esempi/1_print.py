# ==================================================
# ESEMPIO 1 - variabili, print e input
# ==================================================

# Le variabili non vanno dichiarate. Devono solamente essere valorizzate
# Il tipo della variabile non va dichiarato, viene inferito automaticamente in base al valore
var1 = "Hello world!"
var2 = 10
var3 = 3.14
var4 = True

# Stampa
print(var1)
print(type(var1)) # E' possibile verificare il tipo di una variabile con la funzione type


# Stampare più valori (con utilizzo della virgola)
print("Stampa di più valori con la virgola (,)")
print("Valore: ", var1, ", tipo: ", type(var1)) 


# Stampare più valori (utilizzando f-string)
print("Stampa di più valori con f string")
print(f"Valore: {var1}, tipo: {type(var1)}")


# La funzione input
nome = input("Come ti chiami? ")
print("Hai scritto:", nome)
print(f"Ciao {nome}!")

# Il tipo preso da input è sempre string. Necessario castare quando si vuole un int o un float
eta = int(input("Quanti anni hai?"))
print(f"Ciao {nome}, hai {eta} anni")
