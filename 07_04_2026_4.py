#Desarrolle un programa que permita ingresar 3 números distintos y
#  siempre los despliegue ascendentemente  

#Nota: Haga simulaciones con 3 números diferentes  
#Declaracion de variables

numero_1 = 0
numero_2 = 0
numero_3 = 0

numero_1 = int(input("Ingresa el primer número: "))
numero_2 = int(input("Ingresa el segundo número: "))
numero_3 = int(input("Ingresa el tercer número: "))

# Paso 1: ordenar los dos primeros
if numero_1 < numero_2:
    menor = numero_1
    mayor = numero_2
else:
    menor = numero_2
    mayor = numero_1

# Paso 2: ubicar el tercero
if numero_3 < menor:
    print(numero_3, menor, mayor)
else:
    if numero_3 > mayor:
        print(menor, mayor, numero_3)
    else:
        print(menor, numero_3, mayor)

