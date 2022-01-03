#Ejercicio 9.
#Escribir un algoritmo que muestre todas las fichas de dominó, sin repetir

for i in range(0, 8):
    for j in range(0, i+1):
        print("/" +str(i) + "/" +str(j))