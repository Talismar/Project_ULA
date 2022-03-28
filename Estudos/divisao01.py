def multiplicacao(numA, numB):
    a = list(numA)
    b = list(numB)

    lista01 = []
    lista02 = []
    lista03 = []

    for i in range(0,3):
        lista01.append(a[0] & b[i])

    for i in range(0,3):
        lista02.append(a[1] & b[i])

    for i in range(0,3):
        lista03.append(a[2] & b[i])

    carry = [0]
    res = []
    res.append(lista01[0])

    aux = str("{0:b}".format(carry[0] + lista01[1] + lista02[0]))
    if len(aux) == 1:
        aux = "0" + aux 

    res.append(aux[1])
    print(f"{carry[0]}  + ", lista01[1] ," + ", lista02[0], " => ",aux[1])
    carry.append(int(aux[0]))

    aux = str("{0:b}".format(carry[1] + lista01[2] + lista02[1] + lista03[0]))
    if len(aux) == 1:
        aux = "0" + aux 

    res.append(aux[1])
    print(f"{carry[0]}  + ", lista01[2]," + ", lista02[1] ," + ", lista03[0], " => ",aux[1])
    carry.append(int(aux[0]))

    aux = str("{0:b}".format(carry[2] + lista02[2] + lista03[1]))
    if len(aux) == 1:
        aux = "0" + aux 

    res.append(aux[1])
    print(f"{carry[0]}  + ", lista02[2] ," + ", lista03[1], " => ",aux[1])
    carry.append(int(aux[0]))

    res.append(lista03[2])

    print(lista01)
    print(lista02)
    print(lista03)
    res = res[::-1]
    print(res[2:])

def subtracao(numA, numB):
    def negando(x):
        if x == 0:
            return 1
        elif x == 1:
            return 0

    bneg = [1]
    subtracao = []

    def ULA0(a, b):
        aux = str("{0:b}".format(bneg[0] + a + negando(b)))
        if len(aux) == 1:
            aux = "0" + aux

        subtracao.append(aux[1])
        bneg.append(int(aux[0]))
        
    def ULA1(a, b):    
        aux = str("{0:b}".format(bneg[1] + a + negando(b)))
        if len(aux) == 1:
            aux = "0" + aux

        subtracao.append(aux[1])
        bneg.append(int(aux[0]))
        
    def ULA2(a, b):
        aux = str("{0:b}".format(bneg[2] + a + negando(b)))
        if len(aux) == 1:
            aux = "0" + aux

        subtracao.append(aux[1])
        bneg.append(int(aux[0]))
    
    if len(numA[:aux]) == 2:
        numA = "0" + numA[:aux]

    elif len(numA) == 1:
        numA = "00" + numA

    if len(numB) == 2:
        numB = "0" + numB

    elif len(numB) == 1:
        numB = "00" + numB

    a = list(numA)[::-1]
    a = [int(val) for val in a ]
    b = list(numB)[::-1]
    b = [int(val) for val in b ]

    ULA0(a[0], b[0])
    ULA1(a[1], b[1])
    ULA2(a[2], b[2])
    
    return "".join(subtracao[::-1])

dividendo = bin(4)
divisor =   bin(2)
dividendo = dividendo[2:]
divisor = divisor[2:]
quociente = []

if len(dividendo) == 2:
    dividendo = "0" + dividendo

if len(divisor) == 2:
    divisor = "0" + divisor 

aux = 1
aux2 = 0
def escolha(divid):
    global aux
    global aux2
    aux2 = aux

    for i in range(1,4):    
        if int(divid[:i],2) >= int(divisor,2):
            print("Igual ou maior > ",divid[:i])
            aux = i
            break    
    
    if aux2 == aux:
        print("Adicionando ZEROS")
    
    return divid

while aux2 != aux:
    escolha(dividendo)

    resto = dividendo[aux:]
    print("Sobrou > ",resto)

    print("Aux - ", aux)

    sub = subtracao(dividendo, divisor)
    print("Subtração > ",sub)
    
    if sub == "000" and resto == "":
        quociente.append(1)
        break    

    if sub == "001":
        resto = sub + resto
        resto = resto[-3:]
        dividendo = resto
        print("Sobrou > ",resto)
        escolha(resto)

    print(dividendo, " = ", divisor)
    quociente.append(1)

print(quociente[::-1]) 