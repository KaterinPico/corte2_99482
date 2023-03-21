
import math

print('Escoja una de las siguientes opciones:\n ')
print('1. Seno')
print('2. Coseno')
print('3. Tangente')
print('4. Exponencial')
print('5. Logaritmica')
print('6. Salir')
OPC=input('Escoja una opción: ')
if OPC=='1':
    x=int(input('Ingrese un número: ')) 
    Seno=math.sin(x)
    print(Seno)
elif OPC=='2':
    x=int(input('Ingrese un número: '))
    Coseno=math.cos(x)
    print(Coseno)
elif OPC=='3':
    x=int(input('Ingrese un número: '))
    Tangente=math.tan(x)
    print(Tangente)
elif OPC=='4':
    x=int(input('Ingrese un número: '))
    y=int(input('Ingrese el exponente'))
    Expo=x*y
    print(Expo)
elif OPC=='5':
    x=int(input('Ingrese un número: '))
    Logaritmica=math.log(x)
    print(Logaritmica)
else:
    print('Fin del proceso')
