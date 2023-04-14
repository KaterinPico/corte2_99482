class Ciudadano:
    def __init__(self,nombre:str,documento:int,edad:int):
        self.__nombre=nombre
        self.__documento=documento
        self.__edad=edad

        #----------Getters-----------
    def getNombre(self):
            return self.__nombre
    
    def getDocumento(self):
            return self.__documento
    
    def getEdad(self):
            return self.__edad
    
        #------------ Setters ------------
    def setNombre(self,nombre:str):
        self.nombre = nombre

    def setDocumento(self,documento:int):
        self.documento = documento

    def setEdad(self,edad:int):
        self.edad = edad

        #--------Sobrecarga metodo----------
    def reconocimiento(self):
        return 'Ha recibido un reconocimiento'
    
class Docente(Ciudadano):
    def __init__(self, nombre: str, documento: int, edad: int, salonesAsignados: int, \
                 asignatura: str):
         super().__init__(nombre, documento, edad)
         self.__salonesAsignados = salonesAsignados
         self.__asignatura = asignatura

          #------------ Getters ------------
    def getSalonesAsignados(self):
            return self.__salonesAsignados
     
    def getAsignatura(self):
            return self.__asignatura
     
          #------------ Setters ------------
    def setSalonesAsignados(self,salonesAsignados:int):
        self.salonesAsignados = salonesAsignados

    def setAsignatura(self,asignatura:str):
        self.asignatura = asignatura

        #-------------Sobrecarga metodo-----------
    def reconocimiento(self):    
        return 'Tambien recibio un reconocimiento'

class Dentista(Ciudadano):
    def __init__(self, nombre: str, documento: int, edad: int, clinica:str, pacientes:int):
          super().__init__(nombre, documento, edad)
          self.__clinica = clinica
          self.__pacientes = pacientes

          #------------ Getters ------------
    def getClinica(self):
            return self.__clinica
     
    def getPacientes(self):
            return self.__pacientes
     
          #------------ Setters ------------
    def setClinica(self,clinica:int):
        self.clinica = clinica

    def setPacientes(self,pacientes:int):
        self.pacientes = pacientes

class Ingeniero(Ciudadano):
    def __init__(self, nombre: str, documento: int, edad: int, campo:str, proyectosRealizados:int):
          super().__init__(nombre, documento, edad)
          self.__campo = campo
          self.__proyectosRealizados = proyectosRealizados

          #------------ Getters ------------
    def getCampo(self):
            return self.__campo
     
    def getProyectosRealizados(self):
            return self.__proyectosRealizados
     
          #------------ Setters ------------
    def setCampo(self,campo:str):
        self.campo = campo

    def setProyectosRealizados(self,proyectosRealizados:int):
        self.setProyectosRealizados = proyectosRealizados       

def main():

    Profesora = Docente('Carolina Calderón',58774325,36,10,'Informatica')

    print(f'Docente: {Profesora.getNombre()}\n'+ f'Documento: {Profesora.getDocumento()}\n'+\
    f'Edad: {Profesora.getEdad()}\n'+ f'Salones asignados: {Profesora.getSalonesAsignados()}\n'+\
    f'Asignatura: {Profesora.getAsignatura()}\n'+ f'Reconocimiento: {Profesora.reconocimiento()}')

    Odontologo = Dentista('Camilo Gomez',10058947301,32,'CityDent',10)

    print(f'Docente: {Odontologo.getNombre()}\n'+ f'Documento: {Odontologo.getDocumento()}\n'+\
    f'Edad: {Odontologo.getEdad()}\n'+ f'Clinica: {Odontologo.getClinica()}\n'+\
    f'Pacientes: {Odontologo.getPacientes()}')

    Ingeniera = Ingeniero('Carol Mora',1012864327,23,'Mecatronica',8)

    print(f'Ingeniera: {Ingeniera.getNombre()}\n'+f'Documento: {Ingeniera.getDocumento()}\n'+\
    f'Edad: {Ingeniera.getEdad()}\n'+ f'Campo: {Ingeniera.getCampo()}\n'+\
    f'Proyectos realizados: {Ingeniera.getProyectosRealizados()}')
    


if __name__=='__main__':
    main()