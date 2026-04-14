#Desarrolla un programa que permita ingresar 2 números si el primero es mayor que el segundo, 
# lo restamos 
# si no lo multiplicamos. 
# si son iguales se suman

# declaro la variable 
num1 = 0 
num2 = 0 
resta = 0 
multiplicacion = 0 
suma = 0

# si n1 es mayor que n2 este se va restar
num1 = int(input ("Ingresa el primer numero: "))
num2 = int(input( "Ingresa el segundo numero: "))
if num1 > num2: 
       resta = num1 - num2
       print (" La resta de los dos numeros ingresados es: ",resta )
else: 
       if num1 < num2: 
              multiplicacion = num1 * num2
              print ("La multiplicacion de los dos numeros ingresados es: " ,multiplicacion )
       if num1 == num2: 
              suma = num1 + num2
              print("La suma de los dos numeros ingresados es : ", suma)
       

