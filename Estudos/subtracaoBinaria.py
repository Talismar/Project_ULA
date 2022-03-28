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
    print(f"{bneg[0]}  + ", a ," + ", b, " => ",aux[1])
    bneg.append(int(aux[0]))
    
def ULA1(a, b):    
    aux = str("{0:b}".format(bneg[1] + a + negando(b)))
    if len(aux) == 1:
        aux = "0" + aux

    subtracao.append(aux[1])
    print(f"{bneg[1]}  + ", a ," + ", b, " => ",aux[1])
    bneg.append(int(aux[0]))
    
def ULA2(a, b):
    aux = str("{0:b}".format(bneg[2] + a + negando(b)))
    if len(aux) == 1:
        aux = "0" + aux

    subtracao.append(aux[1])
    print(f"{bneg[2]}  + ", a ," + ", b, " => ",aux[1])
    bneg.append(int(aux[0]))

a = [1,1,0]
b = [0,1,0]

ULA0(a[0], b[0])
ULA1(a[1], b[1])
ULA2(a[2], b[2])
    
print("Binary > ","".join(subtracao[::-1]), " - Decimal > ")
print("Overflow > ",bneg[-1])