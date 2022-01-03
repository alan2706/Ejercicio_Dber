#Ejercicio 4
#Para un valor entero positivo que representa una cantidad en segundos, indicar
#su equivalente en minutos, horas y días
segundos = int(input("Ingrese los segundos: "))
dias = segundos // (24 * 60 * 60)
segundos = segundos % (24 * 60 * 60)
horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)
min = segundos // 60
segundos = segundos % 60 
print("Dias: {} - Horas: {} - Minutos: {} - Segundos: {}".format(dias, horas, min, segundos))