from test.models.aluno import Aluno 

class AlunoTest:
    def __init__(self):
        print("___________________ Aluno table operations tests ___________________")
        self.__connection_test()
        
    def __connection_test(self):
        try:
            self.__aluno = Aluno()
        except:
            print(" * Can't connect the table Aluno in postgreSQL :(")
            exit(1)
        
        print(" * Connect at the table Aluno in postgreSQL :)")
    
    def insertTest(self, json):
        self.__n_matricula = self.__aluno.insert(json)
        if self.__n_matricula is None: return False
        else: return True
    
    def getAllTest(self):
        result = self.__aluno.get_all()
        if result is None: return False
        else: return True

    def updateTest(self, json):
        return self.__aluno.update(self.__n_matricula , json)

    def deleteTest(self):
        return self.__aluno.delete(self.__n_matricula )