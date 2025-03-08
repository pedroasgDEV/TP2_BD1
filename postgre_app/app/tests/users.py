from app.utils.tables.users import Users 

class UsersTest:
    def __init__(self):
        print("___________________ Users table operations tests ___________________")
        self.__connection_test()
        
    def __connection_test(self):
        try:
            self.__usr = Users()
        except:
            print(" * Can't connect the table users in postgreSQL :(")
            exit(1)
        
        print(" * Connect at the table users in postgreSQL :)")
    
    def insertTest(self, doc):
        return self.__usr.insert(doc)
    
    def loginTest(self, doc):
        docs_read = self.__usr.login(doc)

        if docs_read is False: return False
        else: return True

    def selectTest(self, regis_id):
        
        docs_read = self.__usr.select(regis_id)

        if docs_read is False: return False
        else: return True
        
    def updateTest(self, regis_id, doc):
        return self.__usr.update(regis_id, doc)
        
    def deleteTest(self, regis_id):
        return self.__usr.delete(regis_id)
    
    def endTestes(self):
        self.__usr.close()