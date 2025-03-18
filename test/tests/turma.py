from test.models.turma import Turma 

class TurmaTest:
    def __init__(self):
        print("___________________ Turma table operations tests ___________________")
        self.__connection_test()
        
    def __connection_test(self):
        try:
            self.__turma = Turma()
        except:
            print(" * Can't connect the table Turma in postgreSQL :(")
            exit(1)
        
        print(" * Connect at the table Turma in postgreSQL :)")
    
    def insertTest(self, json):
        self.__turma_id = self.__turma.insert(json)
        if self.__turma_id is None: return False
        else: return True

    def getAllTest(self):
        result = self.__turma.get_all()
        if result is None: return False
        else: return True

    def updateTest(self, json):
        return self.__turma.update(self.__turma_id, json)

    def deleteTest(self):
        return self.__turma.delete(self.__turma_id)