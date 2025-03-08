from app.utils.tables.admins import Admins 

class AdminsTest:
    def __init__(self):
        print("___________________ Admins table operations tests ___________________")
        self.__connection_test()
        
    def __connection_test(self):
        try:
            self.__adm = Admins()
        except:
            print(" * Can't connect the table admins in postgreSQL :(")
            exit(1)
        
        print(" * Connect at the table admins in postgreSQL :)")
    
    def insertTest(self, doc):
        result = self.__adm.insert(doc)
        
        if result is False: return False
        else : 
            self.__id = result
            return True
            
    def loginTest(self, doc):
        docs_read = self.__adm.login(doc)

        if docs_read is False: return False
        else: return True

    def selectTest(self, id = None):
        
        if id is None: id = self.__id
        
        docs_read = self.__adm.select(id)

        if docs_read is False: return False
        else: return True
        
    def selectAllTest(self):    
        docs_read = self.__adm.select_all()

        if docs_read is False: return False
        else: return True
        
    def updateTest(self, doc, id = None):
        
        if id is None: id = self.__id
        
        return self.__adm.update(id, doc)
        
    def deleteTest(self, id = None):
        
        if id is None: id = self.__id
        
        return self.__adm.delete(id)
    
    def endTestes(self):
        self.__adm.close()