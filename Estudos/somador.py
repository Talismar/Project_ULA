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

def OperAND(x, y):
    print("  X     Y     &")
    print("-"*17)
    for i in range(0,len("{0:b}".format(x))):
        
        if "{0:b}".format(x)[i] == str(1) and "{0:b}".format(y)[i] == str(1):
            print(" ","{0:b}".format(x)[i], " - ", "{0:b}".format(y)[i], " -  1")
        else:
            print(" ","{0:b}".format(x)[i], " - ", "{0:b}".format(y)[i], " -  0")

OperAND(0,1)