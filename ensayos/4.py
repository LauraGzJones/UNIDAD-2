'''Ejercicio 2
Escribe un programa que:

Pida números al usuario hasta que ingrese un 0 (el 0 es la señal de parada)
Vaya sumando todos los números ingresados
Al final imprima la suma total'''

contador = 1
num = 0
suma =0 
num = int (input(f"Ingresa el {contador} numero:"))#se da inicio a la variable num
while num != 0: # esta condicion para cuando se ingresa 0
     num = int (input(f"Ingresa el {contador} numero:")) # es para que se ingrese el numero 
     suma = suma + num 
     contador  = contador + 1 # hace que el contador aumente para que se pueda ingresar el siguiente numero
print (f"la suma es {suma}") #después de que se ingresa el 0, se muestra la suma total de los numeros ingresados 