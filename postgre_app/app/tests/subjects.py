from app.utils.tables.subjects import Subjects 

class SubjectsTest:
    def __init__(self):
        print("___________________ Subjects table operations tests ___________________")
        self.__connection_test()
        
    def __connection_test(self):
        try:
            self.__sub = Subjects()
        except:
            print(" * Can't connect the table subjects in postgreSQL :(")
            exit(1)
        
        print(" * Connect at the table subjects in postgreSQL :)")
    
    def insertTest(self, doc):
        return self.__sub.insert(doc)

    def selectTest(self, subject_code):      
        docs_read = self.__sub.select(subject_code)
        
        if docs_read is False: return False
        else: return True
    
    def selectAllTest(self):    
        docs_read = self.__sub.select_all()

        if docs_read is False: return False
        else: return True
        
    def updateTest(self, subject_code, doc):
        return self.__sub.update(subject_code, doc)
        
    def deleteTest(self, subject_code):
        return self.__sub.delete(subject_code)
    
    def endTestes(self):
        self.__sub.close()