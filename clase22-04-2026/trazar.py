x = 1
while x <= 4:
    z = x
    print( x,end = "->")
    while z != 0:
        print(z,end = ".")
        z = z - 1
    print ("")
    x = x + 1
print ("Fin ")