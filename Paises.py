import  csv
with open('organization_data.csv','rt') as archivo:
    filas= csv.reader(archivo)
    for fila in filas:
        print(fila)

        
       
    