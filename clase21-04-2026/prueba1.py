# Definimos cuántos números vamos a pedir (10 en este caso)
ciclos = 10

# Variable donde guardaremos cada número que ingrese el usuario
numero = 0

# Variable donde guardaremos el número mayor encontrado hasta ahora
mayor = 0

# Contador que usaremos para saber en qué vuelta del ciclo estamos
a = 1

# Repetimos todo lo que está adentro MIENTRAS "a" sea menor o igual a 10
# Es decir, esto se repite 10 veces (una por cada número que pedimos)
while a <= ciclos:

    # Le pedimos al usuario que escriba un número y lo convertimos a entero
    numero = int(input(f"Ingrese un número {a} de {ciclos}: "))

    # Si es la PRIMERA vuelta (a == 1), el mayor es simplemente el primer número
    # porque no tenemos otro con qué comparar todavía
    if a == 1:
        mayor = numero

    # Si NO es la primera vuelta, comparamos con el mayor que ya teníamos
    else:
        # Si el número nuevo es más grande que el mayor actual, lo reemplazamos
        if numero > mayor:
            mayor = numero

    # Le sumamos 1 al contador para pasar a la siguiente vuelta
    a = a + 1

# Cuando el ciclo termina (ya se pidieron los 10 números), mostramos el resultado
print("El número mayor es", mayor)