a = [0,0,1]
b = [1,1,0]

print(a[2] ^ b[2])

if ((a[2] ^ b[2]) == 0) or (a[2] == 1 and b[2] == 1):
    if a[2] == 0 and b[2] == 0:
        carryIn = 0
    else:
        carryIn = 1
else:
    carryIn = 0

print((a[1] ^ b[1]) ^ carryIn)

if ((a[1] ^ b[1]) ^ carryIn == 0) or (a[1] == 1 and b[1] == 1):
    if a[1] == 0 and b[1] == 0:
        carryIn = 0
    else:
        carryIn = 1
else:
    carryIn = 0

print((a[0] ^ b[0]) ^ carryIn)

if ((a[0] ^ b[0]) ^ carryIn == 0) or (a[0] == 1 and b[0] == 1):
    carryIn = 1
else:
    carryIn = 0