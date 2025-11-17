#Registro de asistentes

#Crea un ciclo que solicite nombres hasta que se escriba “FIN”. Al finalizar, muestra:

#    El total de nombres ingresados.
#    Si hay nombres repetidos.

#El programa debe ignorar entradas vacías y evitar usar TRY/EXCEPTION pero buscar alternativas para validaciones.

Lista_Nombre = ["ana", "anna", "cristal", "Zoe", "Cristian", "Flora angelical", "Cristian"]

print("FIN para finalizar")

while True:
    nombre = input("nombre: ")
    if nombre.lower() == "fin":
        break
    if nombre:
        Lista_Nombre.append(nombre)

print(len(Lista_Nombre))

mostrados = set()
for elemento in Lista_Nombre:
    if Lista_Nombre.count(elemento) > 1 and elemento not in mostrados:
        print(elemento, "está repetido", Lista_Nombre.count(elemento), "veces")
        mostrados.add(elemento)