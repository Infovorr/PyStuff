def relprime(a,b):
    q = -1
    r1 = a
    r2 = b
    swap = None
    while (r2 != 0):
        q = r1 // r2
        swap = r2
        r2 = r1 % r2
        r1 = swap
    return r1 == 1

def phi(a,b):
    total = 1
    for i in range(2,a):
        x = relprime(a, i)
        if x == 1:
            total = total + 1
    return total == b
