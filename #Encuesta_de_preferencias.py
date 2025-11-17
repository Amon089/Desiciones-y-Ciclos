#Solicita edad y respuesta a la pregunta: “¿Te gusta programar?” (sí/no). 
# El programa debe repetirse mientras la edad ingresada sea mayor a cero. 
# Al finalizar, muestra cuántas respuestas fueron afirmativas y cuántas negativas. 
# Controla respuestas vacías o incorrectas dentro del ciclo.

print("Bienvenido a la encuesta de preferencias.")

contador_si = 0
contador_no = 0

while True:
    edad = input("¿Que edad tienes? \n(0 para salir): ")

    if not edad.isdigit():
        print("Edad invalida. Ingresa solo numeros.")
        continue

    edad = int(edad)
    if edad <= 0:
        break

    while True:
        gusto = input("¿Te gusta programar? (si/no): ").strip().lower()
        if gusto == "si":
            contador_si += 1
            break
        elif gusto == "no":
            contador_no += 1
            break
        else:
            print("Respuesta invalida. Escribe 'si' o 'no'.")

print("Encuesta finalizada.")
print("Respuestas afirmativas:", contador_si)
print("Respuestas negativas:", contador_no)
