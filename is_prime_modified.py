

def is_prime(a):
    cont = 0
    for i in range(1, a+1):
        if a % i == 0:
            cont += 1
    if cont == 2:
        prim = 1
        return prim
    else:
        primNo = 0
        return primNo

while True:
    try:
        a=int(input("Introduzca un valor: "))
        if a<=0:
            break

        res=is_prime(a)
        if res==0:
            print(0)
        else:
            res==1
            print(1)
    except:
        print(-1)
        print("Tiene un error")


