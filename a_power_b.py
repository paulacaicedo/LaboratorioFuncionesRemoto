def a_power_b(a,b):
    prod=1
    for i in range(1,b+1):
        prod=prod*a
        if i > 63:
            raise ValueError('El numero es muy grande')
            break
    return prod

pote = 0
par = 0
impar = 0
error = 0
while True:
    try:
        a = int(input("Introduzca un valor: "))
        if a == 0:
            break

        b = int(input("Introduzca la potencia: "))
        pote=pote+1

        res = a_power_b(a, b)
        print("El resultado es ",res)
        if res%2==0:
            par=par+1
        else:
            impar=impar+1
    except:
        print("Tiene un error!!!")
        error=error+1


print("El numero de potencias calculadas fue: ",pote)
print("El numero de errores fue: ",error)
print("El numero de resultados pares fue: ",par)
print("El numero de resultados impares fue: ",impar)
