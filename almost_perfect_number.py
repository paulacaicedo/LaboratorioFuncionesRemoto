

def perfect_number(a):
    cont = 0
    for i in range(1, a):
        if a % i == 0:
            d = i
            print("Divisor", d)
            cont = cont+d
        res=cont-a
    if res<=3:
        print(a, "Is a almost-perfect number")
    else:
        print(a, "Is NOT a almost-perfect number")


a = int(input("Introduzca un valor: "))
perfect_number(a)