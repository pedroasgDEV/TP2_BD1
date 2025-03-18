from test.models.professor import Professor 

class ProfessorTest:
    def __init__(self):
        print("___________________ Professor table operations tests ___________________")
        self.__connection_test()
        
    def __connection_test(self):
        try:
            self.__professor = Professor()
        except:
            print(" * Can't connect the table Professor in postgreSQL :(")
            exit(1)
        
        print(" * Connect at the table Professor in postgreSQL :)")
    
    def insertTest(self, json):
        self.__professor_cpf = self.__professor.insert(json)
        if self.__professor_cpf is None: return False
        else: return True

    def getAllTest(self):
        result = self.__professor.get_all()
        if result is None: return False
        else: return True

    def updateTest(self, json):
        return self.__professor.update(self.__professor_cpf, json)

    def deleteTest(self):
        return self.__professor.delete(self.__professor_cpf)