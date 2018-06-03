# creating multiple parent classes

class Mom:
	mom = 'Hey I\'m mom'

class Dad:
	dad = 'Hey there son!'

#pass the multiple parameters of the class names that are supposed to be the super classes
class child(Mom, Dad):
	pass

child_object = child()
print(child_object.mom)
print(child_object.dad)