class Car:
 
    def __init__(self):
        self.__updatesoftware()
 
    def draw(self):
        print 'drawing'
 
    def __updateSoftware(self):
        print 'updating'
 
draw1 = Car()
draw1.draw()
