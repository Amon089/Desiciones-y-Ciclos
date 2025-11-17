#control de acceso

#Pide un nombre de usuario y un código numérico.
#Permite el ingreso solo si el usuario no está en la lista restringida y
#su código cumple al menos una de las siguientes condiciones:

#    Es múltiplo de 2.
#    Termina en 7.

#Debe mostrar un mensaje distinto según el motivo del rechazo. 
# Elabora un diagrama de flujo que represente la decisión principal.

nombre_denegados= input("ingrese el usuario: ").lower()
codigo = int(input("ingrese el código: "))

if nombre_denegados in ("camilo", "val", "mige"):
    print("Acceso denegado usuario restringido")
else:
    if codigo % 2 == 0 or codigo % 10 == 7:
        print("Acceso permitido")
    else:
        print("Acceso denegado: código no válido")
