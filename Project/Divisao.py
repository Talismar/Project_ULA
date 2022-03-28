aux = 0
def Division(Dividendo, Divisor):

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

    dividendo = bin(Dividendo)
    divisor =   bin(Divisor)
    dividendo = dividendo[2:]
    divisor = divisor[2:]
    quociente = []
    dividendo, divisor = verificacao(dividendo, divisor)

    
    def divisao(divid):
        global aux
        global aux2
        aux2 = aux

        for i in range(1,4):    
            "Dividindo por 1 retorna o mesmo valor"
            if int(divisor,2) == 1:
                divid = divid[::-1]
                quociente.append(divid[0])
                quociente.append(divid[1])
                quociente.append(divid[2])
                break
            
            "Dividir por zero retorna None"
            if int(divisor,2) == 0:
                divid = divid[::-1]
                quociente.append("None")
                break
            

            if int(divid[:i],2) >= int(divisor,2):
                
                if len(divid[:i]) == len(divisor) and int(divid[:i],2) == int(divisor,2):
                    quociente.append(1)
                    break

                aux = i
                resto = dividendo[aux:]
                
                sub = subtracao(divid[:i], divisor)

                "4/2 - 6/3 - 5/2"
                if sub == "000":
                    if int(divid[i],2) < int(divisor,2):
                        quociente.append(0)
                    if resto == "00":
                        quociente.append(0)
                    
                    quociente.append(1)   
                    divid = resto

                #5/3
                elif sub == "010":
                    quociente.append(1)   

                #6/3
                elif sub == "001":
                    if resto == "":
                        if int(divid[:i],2) > int(divisor,2):
                            quociente.append(1)
                            break
                        quociente[0] = 0
                        
                    resto = sub + resto
                    resto = resto[-3:]

                    quociente.append(1)   
                    divid = resto

        return divid

    divisao(dividendo)
    return quociente[::-1][-3:]