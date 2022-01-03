#Ejercicio 8.
#Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla
#del 1 hasta la del 10.

numero = int(input("Ingrese elnumero de la tabla que quiere generar "))
for i in range(1, 11):
    print(f'{i} x {numero} = {i * numero}')
    