#Estructuras Iterativas
#Ejercicio 1.
#Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene
#dicho número

numero = int(input("Ingrese el numero entero "))
if numero >=-9 and numero <=9:
    print("El numero contiene un solo digito")
else:
    if numero >=-99 and numero <=99:
        print("El numero contiene dos digitos")
    else:
        if numero >=-999 and numero <=999:
            print("El numero contiene tres digitos")
        else:
            if numero >=-9999 and numero <=9999:
                print("El numero contiene cuatro digitos")
