#Ejercicio 2
#Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es
#capicúa.

numero = int(input("Digite el numero "))
if numero >= 0:
    if str(numero) == str(numero)[::-1]:
        print("El numero " +str(numero)+" es capicua")
    else:
        print("El numero " +str(numero)+" no es capicua")
else:
    print("El numero debe de ser positivo")