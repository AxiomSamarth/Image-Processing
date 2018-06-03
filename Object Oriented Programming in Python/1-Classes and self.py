#create the template or blueprint of the class with the methods and variables
#all the definitions are supposed to have the parameter called self which is nothing but the reference to the object that is 
#calling that particular method.

class ClassName:

# __init__(self) is the constructor for the objects, that performs all the intializations for an object instantiated for this class

  def __init__(self):
    self.name = 'Teddy Winters'

  def create_name(self, name):
    self.name = name

  def display_name(self):
    return self.name

  def saying(self):
    print "Hello %s" % self.name


#This is the way of creating new classes
person_a = ClassName()
person_b = ClassName()

#This is the way of calling upon the methods from the class via that particular object and it's always has an individual action
person_a.create_name('Samarth Deyagond')    
# person_b.create_name('Sagar Deyagond')

#Yet another example
print person_a.display_name(),
person_b.saying()