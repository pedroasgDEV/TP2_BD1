from test.models.disciplina import Disciplina 

class DisciplinaTest:
    def __init__(self):
        print("___________________ Disciplina table operations tests ___________________")
        self.__connection_test()
        
    def __connection_test(self):
        try:
            self.__disciplina = Disciplina()
        except:
            print(" * Can't connect the table Disciplina in postgreSQL :(")
            exit(1)
        
        print(" * Connect at the table Disciplina in postgreSQL :)")
    
    def insertTest(self, json):
        self.__disciplina_codigo = self.__disciplina.insert(json)
        if self.__disciplina_codigo is None: return False
        else: return True

    def getAllTest(self):
        result = self.__disciplina.get_all()
        if result is None: return False
        else: return True


    def updateTest(self, json):
        return self.__disciplina.update(self.__disciplina_codigo, json)

    def deleteTest(self):
        return self.__disciplina.delete(self.__disciplina_codigo)