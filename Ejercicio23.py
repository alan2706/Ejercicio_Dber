#Ejercicio 3.
#Dado un número N determinar si es un número primo.
#Nota: Un número primo es aquel que solo es divisible por 1(uno) y por el mismo.

numero = int(input("Ingrese el numero "))
EsPrimo = True
for i in range(2,numero):
    if numero % i == 0:
        EsPrimo = False
        break
if EsPrimo:
    print("Es numero primo")
else:
    print("No es numero primo")
    