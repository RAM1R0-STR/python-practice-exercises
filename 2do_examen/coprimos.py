def divisores(n):
    ldiv = []
    for i in range(1,n,1):
        div = n%i
        if div == 0:
            ldiv.append(i)
    return ldiv

def coprimos(n1,n2):
    ln1 = divisores(n1)
    ln2 = divisores(n2)
    c = 0
    for elem in ln1:
        if elem in ln2:
            c = c +1
    if c > 1:
        return False
    else:
        return True

print(coprimos(6,8))