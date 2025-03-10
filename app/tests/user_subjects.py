from app.utils.tables.user_subjects import UsrSub 

class UsrSubTest:
    def __init__(self):
        print("___________________ User_subjects table operations tests ___________________")
        self.__connection_test()
        
    def __connection_test(self):
        try:
            self.__usrsub = UsrSub()
        except:
            print(" * Can't connect the table user_subjects in postgreSQL :(")
            exit(1)
        
        print(" * Connect at the table user_subjects in postgreSQL :)")
    
    def insertTest(self, user_id, subject_code):
        return self.__usrsub.insert(user_id, subject_code)

    def verifyTest(self, user_id, subject_code):      
        return self.__usrsub.verify(user_id, subject_code)
        
    def selectAllUsrsTest(self, subject_code):
        docs_read = self.__usrsub.select_all_users(subject_code)

        if docs_read is False: return False
        else: return True
    
    def selectAllSubsTest(self, user_id):
        docs_read = self.__usrsub.select_all_subjects(user_id)

        if docs_read is False: return False
        else: return True
    
    def deleteTest(self, user_id, subject_code):
        return self.__usrsub.delete(user_id, subject_code)
    
    def endTestes(self):
        self.__usrsub.close()