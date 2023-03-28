PM=('Programacion aplicada a sistemas mecatronicos', 'Dia: Martes y Jueves', 'Hora: 1 pm a 3 pm', 'Salón: GO 303', 'Profesor: David Torres')
DI=('Dibujo de ingenieria', 'Dia: Viernes', 'Hora: 9 am a 11 am', 'Salón: GO 302', 'Profesor: Juan Gabriel')
I=('Identidad institucional', 'Dia: Lunes', 'Hora: 9 am a 11 am', 'Salón: DB 406', 'Profesor: Daniel Calderón')
PdV=('Proyecto de vida', 'Dia: Lunes', 'Hora: 11 am a 1 pm', 'Salón: DB 303', 'Profesor: Sin definir')
TFM=('Taller de fisica mecanica', 'Dia: Lunes', 'Hora: 1 pm a 3 pm', 'Salón: DB 306', 'Profesor: Julian Ortiz')
CI=('Calculo integral', 'Dia: Martes y Jueves', 'Hora: 7 am a 9 am', 'Salón: DB 407', 'Profesor: Edwin Acuña')
C=('Circuitos', 'Dia: Martes y Jueves', 'Hora: 11 am a 1 pm', 'Salón: DB 306', 'Profesor: Hernan Pineda')
FM=('Fisica mecanica', 'Dia: Martes y Jueves', 'Hora: 9 am a 11 am', 'Salón: DB 404', 'Profesor: Roberto Bohorques')

opc=''
while opc!='salir':   
    opc=input('¿Que materia desea consultar? ')

    if opc == 'programacion aplicada a sistemas mecatronicos':
        print(PM)

    elif opc == 'dibujo de ingenieria':
        print(DI)

    elif opc == 'identidad institucional':
        print(I)

    elif opc == 'proyecto de vida':
        print(PdV)

    elif opc == 'Taller de fisica mecanica':
        print(TFM)

    elif opc == 'calculo integral':
        print(CI)

    elif opc == 'circuitos':
        print(C)

    elif opc == 'fisica mecanica':
        print(FM)
    


