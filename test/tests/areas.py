from test.models.areas import Areas 

class AreasTest:
    def __init__(self):
        print("___________________ Areas de Interesse table operations tests ___________________")
        self.__connection_test()
        
    def __connection_test(self):
        try:
            self.__areas = Areas()
        except:
            print(" * Can't connect the table Areas de Interesse in postgreSQL :(")
            exit(1)
        
        print(" * Connect at the table Areas de Interesse in postgreSQL :)")
    
    def insertTest(self, json):
        self.__area_id = self.__areas.insert(json)
        if self.__area_id is None: return False
        else: return True

    def getAllTest(self):
        result = self.__areas.get_all()
        if result is None: return False
        else: return True

    def updateTest(self, json):
        return self.__areas.update(self.__area_id, json)

    def deleteTest(self):
        return self.__areas.delete(self.__area_id) 