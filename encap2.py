class Student:
 
    __access = 0
    name = ""
 
    def __init__(self):
        self.__access = 200
        self.name = "satyam"
 
    def draw(self):
        print "access no of given student is  "+str(self.__access)

 
stud = Student()
stud.draw()
stud.access = 10  # will not change variable because its private
stud.draw()
