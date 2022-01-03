#Ejercicio 3
#Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como
#resultado su equivalente en segundos.

horas = int(input("Digite la cantidad de horas "))
min = int(input("Digite la cantidad de minutos "))
segundos1 = horas * 60 * 60
segundos2 = min * 60
segundosT = segundos1 + segundos2
print("La cantidad de segundos es igual a: {}".format(segundosT))