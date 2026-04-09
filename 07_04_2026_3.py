#Desarrolle un programa que permita ingresar 3 números y desplegar siempre el mayor. 

 # Nota: haga simulaciones con 3 números diferentes 
# Declarar las variables
n1 = 0 
n2 = 0
n3 = 0 
#ux ingresa los números
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))
# hay que analizar  cual es el mayor de los tres números ingresados por el usuario
#revisamos el numero 1 
if n1 > n2:  
  if n1 > n3: 
    print (f'El numero mayor es el:,{n1}' ) # si n1 es mayor que  n2 y n3 se cumple la condicion 
  else:              
    print( f'El numero mayor es el : ,{n3}') 
    
else: 
   if n2> n1: # si n2 es mayor que n1 y n3 se cumpliria la condicion 
     if n2 > n3:
      print(f'El numero mayor es el: , {n2}')
     else: # si ninguna se cumple es el n3 el mayor
       print (f'El numero mayor es el:, {n3}')
 
  

