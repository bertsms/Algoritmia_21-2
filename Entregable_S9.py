class Person:
    '''Clase de Persona
    recibe el nombre y apellido como parametro'''
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, clave):
        super().__init__(fname , lname)
        self.__carrera = 'comunicacion'
        self.__clave = clave

    def getClave(self):
        return self.__clave

    def setClave(esta, clave):
        esta.__clave = clave

    def getCarrera(self):
        return self.__carrera 

    def setCarrera(esta, carrera):
        esta.__carrera = 'derecho'

    def printname(self):
        super().printname()
        print("Soy estudiante")

Ana = Person('Ana', 'Pena')
Ana.printname()
print()
Juan = Student('Juan', 'Hernandez', 123435)
Juan.printname()
print('Mi clave es:', Juan.getClave())
print('Mi carrera es:', Juan.getCarrera())
print()
Ximena = Student('Ximena', 'Mora', 896543)
Ximena.printname()
Ximena.setClave(896453)
print('Mi clave es:', Ximena.getClave())
Alondra.setCarrera('derecho')
print('Mi carrera es:', Ximena.getCarrera())