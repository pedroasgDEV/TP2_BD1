from test.models.avaliacao import Avaliacao 

class AvaliacaoTest:
    def __init__(self):
        print("___________________ Avaliacao table operations tests ___________________")
        self.__connection_test()
        
    def __connection_test(self):
        try:
            self.__avaliacao = Avaliacao()
        except:
            print(" * Can't connect the table Avaliacao in postgreSQL :(")
            exit(1)
        
        print(" * Connect at the table Avaliacao in postgreSQL :)")
    
    def insertTest(self, json):
        self.__avaliacao_id = self.__avaliacao.insert(json)
        if self.__avaliacao_id is None: return False
        else: return True

    def getAllTest(self):
        result = self.__avaliacao.get_all()
        if result is None: return False
        else: return True

    def deleteTest(self):
        return self.__avaliacao.delete(self.__avaliacao_id[0], self.__avaliacao_id[1]) 