#clasificación de cliente

#Pide el valor total de una compra y el tipo de membresía. Clasifica al cliente como:
#
#    Premium → monto alto y membresía activa.
#    Frecuente → monto medio o membresía temporal.
#    Regular → cualquier otro caso.
#
#Si el monto es inválido, muestra un mensaje de error.

print("Bienvenido")
valor = int(input("¿Cuál fue el total de la compra?\n"))
membresia = input("¿Tienes membresía? \n(si/no)\n").lower()

if membresia == "si":

    teporal= input("es una membresia temporal? \n(si/no)\n").lower()
    if membresia=="si" and teporal== "no" and valor >= 500001:
        print("usuario primiun")

    elif valor<= 60000 and valor <= 500000:
        print("usuario frecuente.")

    elif  teporal== "si" and valor >=1:
        print("usuario frecuente.")

    elif valor <= 60000 and valor >= 1:
        print("usuario regular")

    else:
        print("monto no valido")

elif membresia == "no":
    if valor >= 1:
        print("usuario regular.")
    else:
        print("monto no valido")

