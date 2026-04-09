edad = 0 
edad = int (input( "ingresa tu edad: "))

if edad < 0 :
   print ("La edad no puede ser menor a cero")
else :
    if edad <18 :
        print ( "Usted es menor de edad ")              
    else:
        if edad > 130 : 
            print ("Su edad supera el limite ") 
        else: print("Usted es mayor de edad")  
        