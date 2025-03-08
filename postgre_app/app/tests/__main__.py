from app.tests.users import UsersTest
from app.tests.admins import AdminsTest
from app.tests.subjects import SubjectsTest
from app.tests.user_subjects import UsrSubTest
from app.tests.admin_subjects import AdmSubTest

usr = UsersTest()

doc = {
    "regis_id": "21.1.4015",
    "name": "Pedro Augusto",
    "email": "pedro.asg@aluno.ufop.edu.br",
    "passwrd": "1234",
    "course": "Ciencia da Computação"
}

if usr.insertTest(doc): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

doc = {
    "email": "pedro.asg@aluno.ufop.edu.br",
    "passwrd": "1234"
}

if usr.loginTest(doc): print(" * Login operation works :)")
else: print(" * Login operation not works :(")

if usr.selectTest("21.1.4015"): print(" * Select operation works :)")
else: print(" * Select operation not works :(")

doc = {
    "name": "Fake",
    "email": "fake@email.com",
}

if usr.updateTest("21.1.4015", doc): print(" * Update operation works :)")
else: print(" * Update operation not works :(")

if usr.deleteTest("21.1.4015"): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

usr.endTestes()

adm = AdminsTest()

doc = {
    "name": "Pedro Augusto",
    "email": "jalnsldasd",
    "passwrd": "1234",
    "derp": "DECOM"
}

if adm.insertTest(doc): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

doc = {
    "email": doc["email"],
    "passwrd": doc["passwrd"]
}

if adm.loginTest(doc): print(" * Login operation works :)")
else: print(" * Login operation not works :(")

if adm.selectTest(): print(" * Select operation works :)")
else: print(" * Select operation not works :(")

if adm.selectAllTest(): print(" * Select All operation works :)")
else: print(" * Select operation not works :(")

doc = {
    "name": "Fake",
    "email": "fake@email.com",
}

if adm.updateTest(doc): print(" * Update operation works :)")
else: print(" * Update operation not works :(")

if adm.deleteTest(): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

adm.endTestes()

sub = SubjectsTest()

doc = {
    "subject_code": "BCC323",
    "name": "Engenharia de Software II",
    "professor": "DANIEL LUDOVICO GUIDONI",
    "derp": "DECOM"
}

if sub.insertTest(doc): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

if sub.selectTest("BCC323"): print(" * Select operation works :)")
else: print(" * Select operation not works :(")

if sub.selectAllTest(): print(" * Select All operation works :)")
else: print(" * Select All operation not works :(")

doc = {
    "professor": "CFRED"
}

if sub.updateTest("BCC323", doc): print(" * Update operation works :)")
else: print(" * Update operation not works :(")

if sub.deleteTest("BCC323"): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

sub.endTestes()

usrsub = UsrSubTest()

if usrsub.insertTest("00.0.0000", "BCC263"): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

if usrsub.verifyTest("00.0.0000", "BCC263"): print(" * Verify operation works :)")
else: print(" * Verify operation not works :(")

if usrsub.selectAllUsrsTest("BCC263"): print(" * Select All Users operation works :)")
else: print(" * Select All Users operation not works :(")

if usrsub.selectAllSubsTest("00.0.0000"): print(" * Select All Subjects operation works :)")
else: print(" * Select All Subjects operation not works :(")

if usrsub.deleteTest("00.0.0000", "BCC263"): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

usrsub.endTestes()

admsub = AdmSubTest()

if admsub.insertTest("1", "BCC263"): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

if admsub.verifyTest("1", "BCC263"): print(" * Verify operation works :)")
else: print(" * Verify operation not works :(")

if admsub.selectAllAdmsTest("BCC263"): print(" * Select All Admins operation works :)")
else: print(" * Select All Users operation not works :(")

if admsub.selectAllSubsTest("1"): print(" * Select All Subjects operation works :)")
else: print(" * Select All Subjects operation not works :(")

if admsub.deleteTest("1", "BCC263"): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

admsub.endTestes()

#6