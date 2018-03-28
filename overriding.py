class Teacher:
  subjects =12
  def marks(self):
    print("this is Teacher class")

class Student(Teacher):
  def marks(self):
    print("override this method")

d=Student()
d.marks()