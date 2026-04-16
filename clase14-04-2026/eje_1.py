''' 0 - 10  → Infante

11 - 18 → Preadolescente

18 → 30 → Adulto joven

30 → 50 → Adulto

50 → +  → adulto mayor'''

#Comentario ilegal
print("hola")

edad = 0 

edad = int (input (" Ingresa tu edad"))
if edad >= 0  and edad <= 10:
    print( "Tu rango de edad es Infante")
if edad >= 11 and edad <= 18:
    print ( "Tu rango de edad es Preadolescente")
if edad >= 19 and edad <=30:
    print("Tu rango de edad es Adulto Joven ")
if edad >= 31 and edad <= 50:
    print ("Tu rango de edad es Adulto")
if edad >= 51:
    print (" Tu rango de edad es Adulto mayor")
else: 
    print("Tu edad es invalida y debe estar entre 0 y 130 ")
