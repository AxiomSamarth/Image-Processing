class parentClass:
	var1 = 'I am var1'
	var2 = 'I am var2'

#This is how we create a child class or a subclass and inherit the attributes, methods of the super class
#by just passing the name of the super class as the parameters

class childClass(parentClass):
	pass


#as usual create the objects and test the inheritance.
parent_object = parentClass()
child_object = childClass()

#print the varibles referred by different objects.
print(parent_object.var1)
print(child_object.var2)