class Animal:
  dog=12
  def __init__(self):
    print ("this is animal class")

  def animalmethod(self):
     print ("this is animalmethod")

  def setvalue(self, value):
     Animal.dog = value

  def getvalue(self):
     print ("value of dog is  :", Animal.dog)


class dog1(Animal): # define child class

  def __init__(self):
     print ("this is dog class")

  def dogmethod(self):
     print ("Calling child method")


d=dog1()
d.dogmethod()
d.animalmethod()
d.getvalue()
d.setvalue(56)
d.getvalue()
