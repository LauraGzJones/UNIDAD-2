edad = 0
edad = float(input("Ingresa tu edad: ")) 

if edad < 0: # si la edad es menor a 0 se considera una edad no válida osea 
    # no acepta edades negativaso
    print("La edad no puede ser negativa")
else:
    if edad != float(edad): # si la edad no es un número entero se considera una edad no válida con
        # el uso de !=
        print("Edad no válida")
    else:
        if edad >= 18:# si la edad es mayor o igual a 18 se considera mayor de edad
            print("Eres mayor de edad")
        else: # si la edad es menor a 18 se considera menor de edad
            print("No eres mayor de edad")


            #hay que revisar el codigo 





        
    # if edad 