#etapa vital y formativa
#Solicita la edad y el nivel educativo de una persona. Clasifica su etapa según las siguientes reglas:
#    Menor de 6 años → Infante
#    Entre 6 y 17 años y estudia → Estudiante escolar
#    Entre 18 y 25 años y estudia → Universitario
#    Mayor de 25 años y trabaja → Adulto activo
#    Mayor de 60 años y no trabaja → Adulto mayor jubilado
#    En cualquier otro caso → No determinado

#Valida que la edad sea coherente y utiliza condiciones encadenadas con operadores lógicos.

print("Bienvenido a la clasificación vital y formativa")
edad = int(input("Qué edad tienes? "))
if edad <= 0 or edad > 120:
    print("Verifica el dato brindado")
elif edad < 6:
    print("Etapa: Infante")
elif 6 <= edad <= 17:
    estudia = input("Estudias? (si/no): ").lower()
    if estudia == "si":
        print("Etapa: Estudiante escolar")
    else:
        print("No determinado")
elif 18 <= edad <= 25:
    estudia = input("Estudias? (si/no): ").lower()
    if estudia == "si":
        print("Etapa: Universitario")
    else:
        print("No determinado")
elif edad > 25 and edad <= 60:
    trabajo = input("Trabajas? (si/no): ").lower()
    if trabajo == "si":
        print("Etapa: Adulto activo")
    else:
        print("No determinado")
elif edad > 60:
    trabajo = input("Trabajas? (si/no): ").lower()
    if trabajo == "no":
        print("Etapa: Adulto mayor jubilado")
    else:
        print("No determinado")
