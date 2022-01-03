#Ejercicio 5.
#Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el
#mayor? y ¿cuál es el segundo mayor?

A = int(input("Ingrese el primer numero: "))
B = int(input("Ingrese el segundo numero: "))
C = int(input("Ingrese el tercer numero: "))
if A > B > C:
    print("El mayor es A")
    print("El segundo mayor es B")
elif A > B < C and A > C:
    print("El mayor es A")
    print("El segundo mayor es C")
elif A < B > C and A > C:
    print("El mayor es B")
    print("El segundo mayor es A")
elif A < B > C and A < C:
    print("El mayor es B")
    print("El segundo mayor es C")
elif A < B < C:
    print("El mayor es C")
    print("El segundo mayor es B")
elif A > B < C and A < C:
    print("El mayor es C")
    print("El segundo mayor es A")
