''' Desarrolle qun programa que permite ingresar 1000 numeros  del ux 
al final tiene que desplegar la suma de estos'''

#declara variables 
x  = 1
suma = 0 
 
while x <= 5:   # es un ciclo.
    num = int(input("Ingresa numero[" + str(x) + "de 5] :"))
    # es el mensaje que se muestra.
 #str(x) → convierte x a texto (porque no puedes juntar número + texto directamente).
    suma = suma + num
    x = x + 1 #es la condición.
print ("suma :", suma)    
 


