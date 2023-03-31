def ecuacion(n,p):
    if n>0:
        print(n,p)
        k=((n*p)+ecuacion(n-1,p))
        return k
    else:
        return 0
    
n=int(input('Ingrese n: '))
p=int(input('Ingrese p: '))
print(ecuacion(n,p))