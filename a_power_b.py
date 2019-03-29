

a=int(input("Introduzca un valor: "))
b=int(input("Introduzca la potencia: "))

def a_power_b(a,b):
    prod=1
    for i in range(1,b+1):
        prod=prod*a
    print("El resultado de la potencia es: ",prod)

a_power_b(a,b)
