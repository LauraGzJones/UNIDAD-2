''' Ejerciio 
Desarrolle un programa que permite ingresar 10 numeros y al finalizar despliegue cual es el 
mayor de ellos 

'''
num  = 0 
contador = 1
mayor = 0

 # while 

while contador < 10:
    num = int(input(f"hola, a continuacion ingresa el numero {contador}: "))
    if num > mayor:
        mayor = num      
    contador = contador + 1   
    print(" EL NUMERO MAYOR ES,",mayor )

    










