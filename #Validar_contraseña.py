#Intentos limitados
#Simula un inicio de sesión con usuario y contraseña predefinidos. 
#Permite hasta tres intentos. Si ambos campos están vacíos, el intento no cuenta.
#Finaliza al alcanzar el máximo o lograr acceso exitoso. 
#Evalúa cada combinación con operadores lógicos y muestra el motivo del fallo.

usuario_correcto = "admin"
contraseña_correcta = "secreto"

for intento in range(3):
    usuario = ""
    while usuario == "":
        usuario = input("Usuario: ")

    contraseña = ""
    while contraseña == "":
        contraseña = input("contraseña: ")

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("acceso concedido!")
        break
    else:
        print("contraseña incorrecta")

else:
    print("demasiados intentos fallidos, acceso denegado.")