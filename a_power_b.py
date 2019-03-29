


def a_power_b(a,b):
    while True:
        if a!=0:
            prod=1
            for i in range(1,b+1):
                prod=prod*a
            print("El resultado de la potencia es: ",prod)
            a = int(input("Introduzca un valor: "))
            b = int(input("Introduzca la potencia: "))
        else:
            break

a=int(input("Introduzca un valor: "))
b=int(input("Introduzca la potencia: "))

a_power_b(a,b)
