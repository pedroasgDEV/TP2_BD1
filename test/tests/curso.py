from test.models.curso import Curso 

class CursoTest:
    def __init__(self):
        print("___________________ Curso table operations tests ___________________")
        self.__connection_test()
        
    def __connection_test(self):
        try:
            self.__curso = Curso()
        except:
            print(" * Can't connect the table Curso in postgreSQL :(")
            exit(1)
        
        print(" * Connect at the table Curso in postgreSQL :)")
    
    def insertTest(self, json):
        self.__curso_codigo = self.__curso.insert(json)
        if self.__curso_codigo is None: return False
        else: return True
    
    def getAllTest(self):
        result = self.__curso.get_all()
        if result is None: return False
        else: return True

    def updateTest(self, json):
        return self.__curso.update(self.__curso_codigo, json)

    def deleteTest(self):
        return self.__curso.delete(self.__curso_codigo)