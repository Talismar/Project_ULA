a = [0,1,0]
b = [0,1,0]
a = a[::-1]
b = b[::-1]

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
#res.append(lista01[1] + lista02[0])

aux = str("{0:b}".format(carry[0] + lista01[1] + lista02[0]))
if len(aux) == 1:
    aux = "0" + aux 

res.append(aux[1])
print(f"{carry[0]}  + ", lista01[1] ," + ", lista02[0], " => ",aux[1])
carry.append(int(aux[0]))

#res.append(lista01[2] + lista02[1] + lista03[0])
aux = str("{0:b}".format(carry[1] + lista01[2] + lista02[1] + lista03[0]))
if len(aux) == 1:
    aux = "0" + aux 

res.append(aux[1])
print(f"{carry[0]}  + ", lista01[2]," + ", lista02[1] ," + ", lista03[0], " => ",aux[1])
carry.append(int(aux[0]))


#res.append(lista02[2] + lista03[1])
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
print(res[::-1])