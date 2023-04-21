def lectura():
    n=open('organization_data.csv','rt')
    data = []
    linea =n.readline()
    while linea != '':
        data.append(linea.rstrip('\n').split(','))
        linea = n.readline()
    n.close()
    return data


def Orden_Paises(data):
    paises=[]
    for i in data[1:]:
        country=i[4]
        if country not in paises:
            paises.append(country)
    paises.sort()
    return paises

def busqueda(data,paises):
    search=int(input('Indice de pais de busqueda: '))
    compañias = []
    empleados = []
    for i in data:
        if i[4] == paises[search-1]:
            compañias.append(i)
            empleados.append(int(i[8]))
    return compañias,empleados

def imprimir(compañias,empleados):
    print(f'\nPaís: {compañias[0][4]}\n')
    
    mayor=empleados.index(max(empleados)) 

    print(f'Empresa con mayor numero de empleados: ')
    
    print(f'Empresa:{compañias[mayor][2]}')
    print(f'Website:{compañias[mayor][3]}')
    print(f'Descripción:{compañias[mayor][5]}')
    print(f'Fundación:{compañias[mayor][6]}')
    print(f'Industria:{compañias[mayor][7]}')
    print(f'Empleados:{compañias[mayor][8]}\n')

    menor=empleados.index(min(empleados)) 

    print(f'Empresa con menor numero de empleados: ')
    
    print(f'Empresa:{compañias[menor][2]}')
    print(f'Website:{compañias[menor][3]}')
    print(f'Descripción:{compañias[menor][5]}')
    print(f'Fundación:{compañias[menor][6]}')
    print(f'Industria:{compañias[menor][7]}')
    print(f'Empleados:{compañias[menor][8]}\n')

    promedio = round(sum(empleados)/len(empleados),2)

    print(f'Promedio empleos: {promedio}')
    print(f'Cantidad de empresas: {len(empleados)}\n')

def main():
    data=lectura()
    paises=Orden_Paises(data)
    data_compañias,data_empleados=busqueda(data,paises)
    imprimir(data_compañias,data_empleados)


if __name__=='__main__':
    main()