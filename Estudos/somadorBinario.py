bneg = [0]
subtracao = []

def ULA0(a, b):
    subtracao.append(int(bneg[0] ^ a ^ b))
    
    bneg.append(int(a & b))

    print(f"{bneg[0]}  + ", a ," + ", b, " => ",bneg[0] ^ a ^ b)
    print(subtracao, bneg)
    
def ULA1(a, b):   
    subtracao.append(int(bneg[1] ^ a ^ b))

    bneg.append(int(a & b))
    print(f"{bneg[1]}  + ", a ," + ", b, " => ",bneg[1] ^ a ^ b)
    print(subtracao, bneg)
    
def ULA2(a, b):
    subtracao.append(int(bneg[2] ^ a ^ b))

    bneg.append(int(a & b))
    print(f"{bneg[2]}  + ", a ," + ", b, " => ",bneg[2] ^ a ^ b)
    print(subtracao)
    
def ula0(a,b):
    lista.append(a[0] ^ b[0] ^ 0)
    print(a[0] & b[0])
    res = (a[0] & b[0])

    lista.append(a[1] ^ b[1] ^ res)
    print(a[1] & b[1])
    res = (a[1] & b[1])

    lista.append(a[2] ^ b[2] ^ res)
    print(a[2] & b[2])
    res = (a[2] & b[2])

a = [1,0,0]
b = [1,0,0]
lista = []
vai = []
carryIn = 0
carryOut = 0

if a[0] == 1 and b[0] == 1:
    vai.append(1)
else:
    vai.append(0)

lista.append(a[0] ^ b[0])

if a[1] == 1 and b[1] == 1:
    vai.append(1)
else:
    vai.append(0)

lista.append(a[1] ^ b[1])

if a[2] == 1 and b[2] == 1:
    vai.append(1)
else:
    vai.append(0)
    
lista.append(a[2] ^ b[2])

print(lista[::-1])
print(vai[::-1])

print([elemA + elemB for elemA, elemB in zip(lista[::-1], vai[::-1])])