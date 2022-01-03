#Ejercicio 5
#Dados tres (3) números, Hacer una aplicación que calcule la resolvente.
import math
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
d= (b*b) - 4 * a * c
if d<0:
   print("No existen soluciones reales")
else:
   x1 = (-b + math.sqrt(d))/(2 * a)
   x2 = (-b - math.sqrt(d))/(2 * a)
   
   print("La solucion de x1 es: ", "{:.2f}".format(x1))
   print("La solucion de x2 es: ", "{:.2f}".format(x2))