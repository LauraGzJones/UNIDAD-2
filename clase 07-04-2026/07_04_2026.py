# Desarrolla un programa que permita que  el ux ingresa su edad 
# # el sistema despliegue si este es mayor o menor de edad  
# declara la variable edad
edad = 0 
# pide al usuario que ingrese su edad
edad = int(input("Ingresa tu edad :"))
#se analiza si la edad es mayor o igual a 18 para determinar si es mayor de edad
if edad >= 18: # si la edad es mayor o igual a 18 se considera mayor de edad
    print("Eres mayor de edad")

else:
    print("No eres mayor de edad")

# ingresa al programa que el maximo de edad es 130 años
if edad > 130:  # si la edad es mayor a 130 se considera una edad
    print("Edad no valida")


#programa basico que solo admite edades enteras y no negativas 