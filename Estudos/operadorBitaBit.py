from os import system 
system("clear")
x = 10 #00111100
y = 5  #00001101

#print("Resultador do operador &: ", x & y) #00001100
#print("Resultador do operador |: ", x | y) #00111101
#print("Resultador do operador << : ", x << 2) #111100
#print("Resultador do operador >> :", x >> 2) #00001111
#print("XOR: ", x ^ y)
#print(bin(15))
#print("NOT: ", ~y)
#print(8 ^ 2)
#print(a)
#print(bin(a) + bin(a))

def soma():
    a = int(input("num 1 > "))
    b = int(input("num 2 > "))
    while (a != 0):
        c = b & a
        print(c)
        b = b ^ a
        print(b)
        c = c << 1
        print("Carry > ",c)
        a = c

    return f"Soma: {b}"

def OperAND(x, y):
    print("  X     Y     &")
    print("-"*17)
    for i in range(0,len("{0:b}".format(x))):
        
        if "{0:b}".format(x)[i] == str(1) and "{0:b}".format(y)[i] == str(1):
            print(" ","{0:b}".format(x)[i], " - ", "{0:b}".format(y)[i], " -  1")
        else:
            print(" ","{0:b}".format(x)[i], " - ", "{0:b}".format(y)[i], " -  0")

def OperOR(x, y):
    print("  X     Y     |")
    print("-"*17)
    for i in range(0,len("{0:b}".format(x))):
        
        if "{0:b}".format(x)[i] == str(1) and "{0:b}".format(y)[i] == str(1):
            print(" ","{0:b}".format(x)[i], " - ", "{0:b}".format(y)[i], " -  1")
        
        elif ("{0:b}".format(x)[i] == str(1) and "{0:b}".format(y)[i] == str(0)) or ("{0:b}".format(x)[i] == str(0) and "{0:b}".format(y)[i] == str(1)):
            print(" ","{0:b}".format(x)[i], " - ", "{0:b}".format(y)[i], " -  1")
        
        else:
            print(" ","{0:b}".format(x)[i], " - ", "{0:b}".format(y)[i], " -  0")

def OperNOT(x):
    print("  X     ~")
    print("-"*11)
    for i in range(0,len("{0:b}".format(x))):
        
        if "{0:b}".format(x)[i] == str(1):
            print(" ","{0:b}".format(x)[i], " -  0")
        
        else:
            print(" ","{0:b}".format(x)[i], " -  1")

def OperXOR(x, y):
    print("  X     Y     |")
    print("-"*17)
    for i in range(0,len("{0:b}".format(x))):
        
        if "{0:b}".format(x)[i] == str(1) and "{0:b}".format(y)[i] == str(1):
            print(" ","{0:b}".format(x)[i], " - ", "{0:b}".format(y)[i], " -  1")
        
        elif ("{0:b}".format(x)[i] == str(1) and "{0:b}".format(y)[i] == str(0)) or ("{0:b}".format(x)[i] == str(0) and "{0:b}".format(y)[i] == str(1)):
            print(" ","{0:b}".format(x)[i], " - ", "{0:b}".format(y)[i], " -  1")
        
        else:
            print(" ","{0:b}".format(x)[i], " - ", "{0:b}".format(y)[i], " -  0")

#OperOR(2,4)
#OperAND(2,3)
#OperNOT(4)


#print(1 & 1)
# print(soma())
#print(subtract(8,7))