


def is_prime(a):
    cont = 0
    for i in range(1, a+1):
        if a % i == 0:
            cont += 1
    if cont == 2:
        print(a, "Is a prime number")
    else:
        print(a, "Is NOT a prime number")


a=int(input("Introduzca un numero: "))
is_prime(a)
