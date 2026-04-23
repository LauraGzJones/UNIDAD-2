cont = 1  # contador empieza en 1
n = 0     # variable para guardar el numero ingresado

while cont <= 10:  # repite 10 veces (1 al 10)
    
    n = int(input("ingresa el numero [" + str(cont) + " de 10] : "))
    # pide un numero y muestra en que turno vas
    # str(cont) convierte el numero a texto para unirlo
    # ejemplo: "ingresa el numero [1 de 10]"
    
    if cont == 1:        # si es el PRIMER numero
        if n > 0:        # si es valido (mayor que 0)
            suma = n     # CREA la variable suma con ese numero
        else:            # si es invalido
            print("Numero ingresado invalido")
            cont = cont - 1  # resta 1 para repetir el turno
    
    else:                # si es el 2do, 3ro... numero
        if n > 0:        # si es valido
            suma = suma + n  # ACUMULA al suma existente
        else:            # si es invalido
            print("Numero ingresado invalido")
            cont = cont - 1  # resta 1 para repetir el turno
    
    cont = cont + 1  # avanza al siguiente turno
    # ojo: si fue invalido, cont bajo 1 y subio 1
    # quedando igual → repite el mismo turno

print(f"Suma total de numeros es {suma}")
# imprime el resultado final fuera del while
