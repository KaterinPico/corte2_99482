import random
L=[random.randint(1, 50)] 
i=1
while i<10:
  x=random.randint(1,50)
  if x not in L:
    L.append(x)
    i+=1
print(L)
#print(sorted(L))

mayor=L[0]
for x in range(1,10):
    if L[x]>mayor:
        mayor=L[x]
print(f'El numero mayor es: {mayor}')

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Imprimir los números primos en la lista

for num in L:
    if es_primo(num):
        print(f"Número primo en la lista: {num}")





    

 