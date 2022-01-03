#Ejercicio 9
#Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho
#número

numero = int(input("Ingrese el numero: "))
if numero >= 1 and numero <= 12:
    if numero == 1:
        print("El mes correspondiente es Enero")
    if numero == 2:
        print("El mes correspondiente es Febrero")
    if numero == 3:
        print("El mes correspondiente es Marzo")
    if numero == 4:
        print("El mes correspondiente es Abril")
    if numero == 5:
        print("El mes correspondiente es Mayo")
    if numero == 6:
        print("El mes correspondiente es Junio")
    if numero == 7:
        print("El mes correspondiente es Julio")
    if numero == 8:
        print("El mes correspondiente es Agosto")
    if numero == 9:
        print("El mes correspondiente es Septiembre")
    if numero == 10:
        print("El mes correspondiente es Octubre")
    if numero == 11:
        print("El mes correspondiente es Noviembre")
    if numero == 12:
        print("El mes correspondiente es Diciembre")
else:
    print("Numero incorrecto, vuelva a digitar")