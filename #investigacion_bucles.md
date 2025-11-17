# Investigacion sobre Bucles

## 1. Diferencias entre un bucle controlado por contador y un bucle controlado por condicion

### Bucle controlado por contador

* Tiene un numero definido de repeticiones.
* Se usa un contador que avansa en cada ciclo.
* Exemplo tipico: `for`.

### Bucle controlado por condicion

* Se ejecuta mientras una condicion logica sea verdadera.
* No siempre se save cuantas veces repetira.
* Exemplo tipico: `while`.

---

## 2. Ejemlos cotidianos de cada tipo de bucle

### Bucle controlado por contador (for)

* Contar 10 repeticiones en el gimnacio.
* Revisar una lista de 20 estudiantes.
* El bucle for es para que el creador del codigo tenga un "control" limitando el bucle a una cantidad de "interacion".

### Bucle controlado por condicion (while)

* Seguir regando una planta mientras la tierra este seca.
* Seguir llamando a una persona mientras no responda.
* El bucle while se usa para que el usuario tenga mas "libertad" al interactuar o asta que se cumpla una condicion espesifica.

---

## 3. Cuando es mas apropiado usar while en lugar de for

* Cuando no conocemos cuantas repeticiones seran necesarias.
* Cuando la repeticion depende de un evento externo.
* Exemplo: esperar asta que el usuario ingrese un dato valido.

---

## 4. Que es un bucle infinito, como prevenirlo y como detectarlo

### Bucle infinito

Ocurre cuando una condicion nunca se buelve falsa, haciendo que el ciclo no termine.

### Como prevenirlo

* Asegurar que la condicion cambie dentro del ciclo.
* Modificar correctamente las varibles usadas en la condicion.

### Como detectarlo

* El programa no abansa.
* La consola sigue imprimiendo sin parar.
* El sistema se buelve lento o se congela.

---

## 5. Funcion de las sentencias break y continue

### break

Detiene por completo el ciclo y sale immediatamente.

### continue

Salta la iteracion actual y continua con la siguiente buelta del ciclo.

---

## 6. Error logico mas comun al usar while y como evitarlo

### Error comun

No actualizar la varible que controla la condicion, generando un bucle infinito.

### Como evitarlo

* Verificar que la varible se modifique dentro del ciclo.
* Revisar la condicion antes de ejecutar.
* Provar con valores de entrada simples para validar el comportamiento.
