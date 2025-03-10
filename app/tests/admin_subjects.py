from app.utils.tables.admin_subjects import AdmSub 

class AdmSubTest:
    def __init__(self):
        print("___________________ Admin_subjects table operations tests ___________________")
        self.__connection_test()
        
    def __connection_test(self):
        try:
            self.__admsub = AdmSub()
        except:
            print(" * Can't connect the table admin_subjects in postgreSQL :(")
            exit(1)
        
        print(" * Connect at the table admin_subjects in postgreSQL :)")
    
    def insertTest(self, admin_id, subject_code):
        return self.__admsub.insert(admin_id, subject_code)

    def verifyTest(self, admin_id, subject_code):      
        return self.__admsub.verify(admin_id, subject_code)
        
    def selectAllAdmsTest(self, subject_code):
        docs_read = self.__admsub.select_all_admins(subject_code)

        if docs_read is False: return False
        else: return True
    
    def selectAllSubsTest(self, admin_id):
        docs_read = self.__admsub.select_all_subjects(admin_id)

        if docs_read is False: return False
        else: return True
    
    def deleteTest(self, admin_id, subject_code):
        return self.__admsub.delete(admin_id, subject_code)
    
    def endTestes(self):
        self.__admsub.close()