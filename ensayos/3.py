''' 
Escribe un programa que:

Pida 5 números al usuario
Si el número es positivo, imprima "el numero es positivo"
Si es negativo, imprima "el numero es negativo"
Si es cero, imprima "el numero es cero"'''

contador = 1
num = 0 
while contador <= 5: 
                                                       
    num = int(input (f"ingresa el {contador} numero:"))
    contador = contador + 1
    if num > 0 :
        print ("El numero es positivo")
    else:
        if num < 0 :
            print ("El numero es negativo")
        else:
            print ("El numero es cero")