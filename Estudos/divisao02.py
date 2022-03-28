def verificacao(A, B):
    if len(A) == 2:
        A = "0" + A

    if len(B) == 2:
        B = "0" + B 
    
    if len(A) == 1:
        A = "00" + A

    if len(B) == 1:
        B = "00" + B 

    return [A, B]

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
    
    numA, numB = verificacao(numA, numB)

    a = list(numA)[::-1]
    a = [int(val) for val in a ]
    b = list(numB)[::-1]
    b = [int(val) for val in b ]

    ULA0(a[0], b[0])
    ULA1(a[1], b[1])
    ULA2(a[2], b[2])
        
    return "".join(subtracao[::-1])

dividendo = bin(5)
divisor =   bin(1)
dividendo = dividendo[2:]
divisor = divisor[2:]
quociente = []
dividendo, divisor = verificacao(dividendo, divisor)

aux = 0
def divisao(divid):
    global aux
    global aux2
    aux2 = aux

    for i in range(1,4):    
        if int(divid[:i],2) >= int(divisor,2):
            print("Dividendo > ",divid[:i], " Divisor > ", divisor)
            
            if len(divid[:i]) == len(divisor) and int(divid[:i],2) == int(divisor,2):
                quociente.append(1)
                break

            aux = i
            resto = dividendo[aux:]
            print("Sobrou > ",resto)
             
            sub = subtracao(divid[:i], divisor)
            print("Subtração > ",sub)

            "4/2 - 6/3 - 5/2"
            if sub == "000":
                if int(divid[i],2) < int(divisor,2):
                    quociente.append(0)
                quociente.append(1)   

            #5/3
            elif sub == "010":
                quociente.append(1)   
                print("Aqui",sub)

            #6/3
            elif sub == "001":
                resto = sub + resto
                resto = resto[-3:]
                quociente.append(1)   
                divid = resto
                print("Sobrou > ",resto)

    return divid

divisao(dividendo)
print(quociente[::-1][-2:]) 