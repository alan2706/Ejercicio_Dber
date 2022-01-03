#Ejercicio 5.
#Dado un número entero N que representa una contraseña y asumiendo que una
#contraseña debe tener al menos 10 dígitos para ser segura, determine si la
#contraseña ingresada por el usuario es correcta, de no serlo debe pedirla
#nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta
#mostrar un mensaje de éxito al usuario, por salida estándar.

def contraseña(n,n1):
    n=int(input("ingrese una contraseña que tenga más de 10 digitos: "))
    digitos=len(str(n))
    if digitos >= 10:
        print("la contraseña es segura")
    else:
        print("la contraseña no es segura")
        return n
    n1=int(input("ingrese la contraseña: "))
    if n1==n:
        print("la contraseña es correcta ")
    
contraseña(0,0)
