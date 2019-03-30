

def perfect_number(a):
    cont = 0
    for i in range(1, a):
        if a % i == 0:
            d = i
            print("Divisor", d)
            cont = cont+d
    if cont == a:
        print(a, "Is a perfect number")
    else:
        print(a, "Is NOT a perfect number")


a = int(input("Introduzca un valor: "))
perfect_number(a)
