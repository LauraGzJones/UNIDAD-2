''' 5. Suma de números
Pide 5 números y muestra la suma total.'''

contador = 1  # repite en el while el parametro para que solo se pidan 5 numeros 
num =0
suma = 0

while contador <= 5:
    num = int (input (f"ingresa el numero {contador} :"))
    suma = suma + num
    contador = contador + 1

    print(" la suma es ", suma) 