#Desarrolla un sistema or onsola que smule el contrl de uavivenda:
#
#    Menú co opciones para encender luces, actiar calefacción, ver estado o salir.
#    Las luces solo pueden encenderse si es de noche.
#    La calefacción solo puede activarse si la temperatura es menor a 18 °C y ls uces están encends
#    El sistemadebe conservar el estado entre acciones y validar combinaciones imposibles.
#
#cluye un diagrama de flujo que muesre la lógica de las condicions pricipales.

print("=== Sistema de Control de Vivieda ===")

luces_encendidas = False
calefaccion_activa = False

while True:
    noche = input("Es de noche? \nseleciona:(si/no): ").strip().lower()
    if noche in ("si", "no"):
        noche = (noche == "si")
        break
    print("Respuesta invalida. Escribe si/no.")

while True:
    temperatura = input("Temperatura actul (C): ")
    if temperatura.replace(".", "", 1).isdigit():
        temperatura = float(temperatura)
        break
    print("Ingrsa un numero valido.")

while True:
    print("\n--- MENU ---")
    print("1. Encender luces")
    print("2. Activar calefacsion")
    print("3. Ver estdo")
    print("4. Salir")

    opcion = input("Elige una opsion: ")

    if opcion == "1":
        if noche:
            if not luces_encendidas:
                luces_encendidas = True
                print("Luces encendidas.")
            else:
                print("Las luces ya estan ensendidas.")
        else:
            print("No es de noche. No puedes encender las luces.")

    elif opcion == "2":
        if temperatura < 18:
            if luces_encendidas:
                if not calefaccion_activa:
                    calefaccion_activa = True
                    print("Calefacsion activada.")
                else:
                    print("La calefacsion ya estava activa.")
            else:
                print("No puedes activar la calefacsion si las luces estan apagdas.")
        else:
            print("La temperatura es mayor o igual a 18C. No se puede activar calefacsion.")

    elif opcion == "3":
        print("\n--- ESTADO DE LA VIVIENDA ---")
        print("Luces:", "Encendidas" if luces_encendidas else "Apagadas")
        print("Calefacsion:", "Activa" if calefaccion_activa else "Inactiva")
        print("Es de noche:", "Si" if noche else "No")
        print(f"Temperatura: {temperatura} C")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opsion invalida. Intenta de nuevo.")
