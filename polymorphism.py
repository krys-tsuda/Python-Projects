


# Parent class user
class User:
    name = "Jane Doe"
    email = "handle@school.com"
    password = "123abc"
    
    def getLogin(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Hello, welcome back!")
        else:
            print("Your email and password do not match.")
        

# Child class parent
class Staff(User):
    badge_id = "123456"
    class_department = "Technology"

    # Same as the parent method except badge_id is used istead of email.
    def getLogin(self):
        entry_name = input("Enter your name: ")
        entry_badge_id = input("Enter your badge id: ")
        entry_password = input("Enter your password: ")
        if (entry_badge_id == self.badge_id and entry_password == self.password):
            print("Hello, welcome back!")
        else:
                print("Your badge_id and password do not match.")
    

# Child class student
class Student(User):
    student_id = 654321
    student_grade = 10

    #same as parent except uses student_id instead of name.
    def getLogin(self):
        entry_student_id = input("Enter your student_id: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Hello, welcome back!")
        else:
            print("Your email and password do not match.")


student = Student()
student.getLogin()

teacher = Staff()
teacher.getLogin()






