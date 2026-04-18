'''El ux Indica hasta donde quieres que llegue la serie de numeros, 
while con sep y end 
un ciclo dentro de otro ciclo 
que por consola imprima una  piramide de numeros ''' 



serie = 0 
contador = 1
ciclo = 1

# Pedimos hasta dónde llega la serie
serie = int(input("Ingrese hasta donde llega la serie: "))

# Este while controla las filas (1 hasta serie)
while contador <= serie:
    # Imprime el número de la fila
    print(contador, " ", end=" ")
    
    # Reinicia el ciclo interno en cada fila
    ciclo = 1
    
    # Este while imprime los números desde 1 hasta contador
    while ciclo <= contador:
        print(ciclo, end=" ")
        ciclo = ciclo + 1  # Aumenta el ciclo
    
    print()  # Salto de línea
    
    contador = contador + 1  # Pasa a la siguiente fila