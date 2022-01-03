#Ejercicio 6
#Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.
import math
a = int(input("Ingrese el valor del primer lado: "))
b = int(input("Ingrese el valor del segundo lado: "))
d = (a * a)+(b * b)
c = (math.sqrt(d))
print("El valor de la hipotenusa es: ", "{:.2f}".format(c))
