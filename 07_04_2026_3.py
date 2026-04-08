#Desarrolle un programa que permita ingresar 3 números y desplegar siempre el mayor. 

 # Nota: haga simulaciones con 3 números diferentes 
# Declarar las variables
numero_1 = 0 
numero_2 = 0
numero_3 = 0 
#ux ingresa los números
numero_1 = int(input("Ingresa el primer número: "))
numero_2 = int(input("Ingresa el segundo número: "))
numero_3 = int(input("Ingresa el tercer número: "))
# hay que analizar  cual es el mayor de los tres números ingresados por el usuario
if numero_1 > numero_2 > numero_3: # si el primer número es mayor que el segundo y el tercer número
    print("El número mayor es: ", numero_1)
else: 
    if numero_2 > numero_1 > numero_3: # si el segundo número es mayor que el primer y el tercer número
        print("El número mayor es: ", numero_2)
    else :
        if numero_3 > numero_1 > numero_2: # si el tercer número es mayor que el primer y el segundo número
            print("El número mayor es: ", numero_3)
        else:
            print("Los números son iguales") # si los tres números son iguales se despliega este mensaje

