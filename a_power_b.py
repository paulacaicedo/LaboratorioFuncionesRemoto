def a_power_b(a,b):
    prod=1
    for i in range(1,b+1):
        prod=prod*a
        if i > 63:
            raise ValueError('El numero es muy grande')
            break
    return prod

while True:
    try:
        a = int(input("Introduzca un valor: "))

        if a == 0:
            break

        b = int(input("Introduzca la potencia: "))

        res = a_power_b(a, b)
        print("El resultado es ",res)

    except:
        print("Tiene un error!!!")