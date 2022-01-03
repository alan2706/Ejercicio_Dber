#Ejercicio 4.
#Construya un programa que dado un valor entero N, haga el cálculo de la función
#factorial utilizando estructuras iterativas.

num=int(input("ingrese el numero: "))
producto=1
i=2
while i <= num:
    producto = producto * i
    i=i+1
print("el número factorial es: {}".format(producto))