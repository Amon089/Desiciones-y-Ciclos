#Participante elegible

#Solicita la edad, si tiene licencia de conducción y si posee vehículo propio.
#Determina si la persona puede participar en una competencia, aplicando las siguientes condiciones:

#    Edad mínima de 18 años.
#    Licencia vigente.
#    Vehículo propio o préstamo autorizado.

#Evalúa con combinaciones de and y or para determinar si es Apto o No apto. 


#.sdigit() se usa para "marcar error cuando el usuario ingrese un valor diferente a un numero entero"

#print("miremos si eres elegible")
#edad_ = input("¿Qué edad tienes? ")
#if not edad_.isdigit():
#    print("Error: el dato brindado es inválido")
#    exit()
#
#edad = int(edad_)
#
#if edad<18:
#    print("no eres elegible")
#    exit()
#print("perfecto estamos un poco mas serca!!")
#
#
#pase= input("tienes pase para condisir? \n (si/no)").lower()
#if pase== "no":
#    print("no eres elegible")
#    exit()
#vigencia=input("esta vigente? \n (si/no)").lower()
#if vigencia=="no":
#    print("no eres elegible")
#    exit()
#
#carro=input("tienes carro? \n (si/no)").lower()
#if carro== "no":
#    print("no eres elegible")
#    exit()
#
#propio=input("es propio? \n (si/no)").lower()
#if propio== "si":
#    print()
#
#prestamo=input("es un prestamo auorisado? \n (si/no)").lower()
#if prestamo=="si":
#    print()
#    
#if edad>18 and vigencia=="si" and carro=="si" and prestamo== "si" or propio=="no":
#    print("cumples, puedes participar")