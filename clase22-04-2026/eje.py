''' DESARRROLLE UN PROGRAMA QUE PERMITA INGRESAR 10 NUMEROS POSITIVOS
SI EL UX INGRESA NEGATIVO EL PROGRAMA DEBE MOSTRAR UN MENSAJE DE ERROR Y NO SE CONSIDERA VALIDO,
PEDIR OTRO
AL FINAL DE LA CARGA DE LOS 10 NUMEROS NECESITAMOS MOSTRAR LA SUMA DE LOS NUMEROS '''

contador = 1
num = 0 
suma = 0
while contador <= 10 :
    num = int (input (f"ingresa el {contador} numero:"))
    if num <0 :
        print (" El numero es negativo,ingresa otro numero")
    else: 
        suma = suma + num 
        contador = contador + 1
    print (f"El resultado de la suma es {suma}")
