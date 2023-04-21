class Ciudadano:
    def __init__(self):
        self.__nombre=None
        self.__documento=None
        self.__edad=None

    #----------Getters-----------
    def getNombre(self):
            return self.__nombre
    
    def getDocumento(self):
            return self.__documento
    
    def getEdad(self):
            return self.__edad
    
        #------------ Setters ------------
    def setNombre(self,nombre:str):
        self.__nombre = nombre

    def setDocumento(self,documento:int):
        self.__documento = documento

    def setEdad(self,edad:int):
        self.__edad = edad

        #-----------Metodo-------------
    def esMayordeEdad(self):
        Edad=self.__edad
        if Edad<18:
             return str('Es menor de edad')
        else:
             return str('Es mayor de edad')

         
def main():
    persona1 = Ciudadano()
    persona1.__nombre='Katerin'
    persona1.__documento=1013589128
    persona1.__edad=17

    persona2 = Ciudadano()
    persona2.nombre='Maria Perez'
    persona2.__documento=52669748
    persona2.__edad=39

    persona3 = Ciudadano()
    persona3.nombre='Julian Dominguez'
    persona3.__documento=1000569785
    persona3.__edad=28

if __name__=='__main__':
     main()
