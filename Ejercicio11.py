#Estructuras De Control de Flujo de Datos
#Ejercicio 1

#Todos los años que se dividen exactamente entre 400, o que son divisibles
#exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos.
#Usando estas premisas crea un algoritmo que lea una fecha como un número
#entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si
#el mismo es un año bisiesto o no.
print("Va ingresar el año en formato ddmmaaaa")
dia = int(input("Digite el dia"))
mes = int(input("Digite el mes"))
año = int(input("Digite el año"))
if (dia > 31) or (dia < 1):
    print("Error, digite bien el dia")
if (mes > 12) or (mes < 1):
    print("Error, digite bien el mes") 
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("El año ",año," es bisiesto")
        else:
            print("El año ",año," no es bisiesto")
    else:
        print("El año ",año," es bisiesto")
else:
    print("El año ",año," no es bisiesto")