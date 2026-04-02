# '''C)	Desarrolle un programa que permita ingresar 3 notas y al finalizar 
# #despliegue el promedio.'''

n1 = 0
n2 = 0
n3 = 0
pro = 0

n1 = float(input("Ing. 1ra nota :"))
n2 = float(input("Ing. 2da nota :"))
n3 = float(input("Ing. 3ra nota :"))

pro = (n1 + n2 + n3) / 3
#print(f"Promedio {pro}") # imprime promedio 
# se necesita saber si el promedio es mayor o igual a 4.0 para aprobar
if pro >= 4.0:  
 print ("Aprobaste con un promedio de ", pro) # si el promedio es mayor o igual a 4.0
 #se aprueba
else:
    print ("Reprobaste con un promedio de ", pro) # si el promedio es menor a 4.0
    #se reprueba
print("Fin del programa")