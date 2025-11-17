# Análisis numérico
# Solicita tres números enteros y determina:
# 
#     Si los tres son positivos.
#     Si al menos uno es negativo.
#     Si exactamente uno es cero.
# 
# Debe analizar todas las combinaciones mediante condiciones encadenadas.


a = int(input("Ingrese numero 1: "))
b = int(input("Ingrese numero 2: "))
c = int(input("Ingrese numero 3: "))


if a > 0 and b > 0 and c > 0:
    print("Los tres son positivos")

elif a < 0 or b < 0 or c < 0:
    print("Hay uno negativo")

elif a == 0 or b == 0 or c == 0:
    print("Uno es 0")

else:
    print("No es un numero")