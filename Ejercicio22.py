#Ejercicio 2.
#Dado un número, determine si es capicúa.
#Nota: un número capicúa es aquel que se lee igual hacia adelante que hacia atrás. 

numero = int(input("Digite el numero "))
if numero >= 0:
    if str(numero) == str(numero)[::-1]:
        print("El numero " +str(numero)+" es capicua")
    else:
        print("El numero " +str(numero)+" no es capicua")
else:
    print("El numero debe de ser positivo")