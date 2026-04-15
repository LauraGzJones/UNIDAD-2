''' Operadores Lógicos 
and, or, not, xor ( se ocupa en cifrado y encripatcion )
Estos,simplifican las condiciones.

AND es un operador lógico que sirve para unir condiciones.
   Cuando trabajamos con AND "tabla de verdad"
   todo tiene que ser verdadero.
   
   Ejemplo 
   if n1> n2 and n1>n3 unir las condiciones 
   🔹 and (Y)👉 Solo es verdadero si ambos son verdaderos

OR uno tiene que ser verdadero para que se cumpla la condicion

🔹 or (O)👉 Es verdadero si al menos uno es verdadero

🔹 not (NO)👉 Invierte el valor: cambia de un valor a otro 
True → False
False → True 
(algebra boolezna)
|
 a   | b | a and b
   .v. | v | v
   .v. | f | f
   .f. | v | f
   .f. | f | f

   a   | b | a or b
   .v. | v | v
   .v. | f | f
   .f. | v | f
   .f. | f | f

 a | not a
   v   f
   f   v

 
 exadecimal :0 1 2 3 4 5 6 7 8 9 A B C D E F
 Tarea: Investigar númemros binarios, suma, 
 conversión de decimal a binario y binario a decimal, hexadecimal.

# Ejercicio de mayor de 3 numeros 
numA = int(input("1er número : "))
numB = int(input("2do número : "))
numC = int(input("3er número : "))

if numA > numB and numA > numC:
   print(numA)
else:
   if numB > numC:
      print(numB)
   else:
      print(numC) '''



edad = int(input("Edad : "))

ad = int(input("Edad : "))

if edad > 0 and edad < 130: # 0 < edad < 130
   if edad <= 18:
      print("mayor")
   else:
      print("menor")
else:
   print("!!!...Edad inválida, debe esta entre cero y 130...!!!")
