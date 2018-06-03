class parent:
	var1 = 'Bacon'
	var2 = 'Snausage'

class child(parent):
	var2 = 'toast'

parent_object = parent()
child_object = child()

print(parent_object.var2)
print(child_object.var2)