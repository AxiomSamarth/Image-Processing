# this is how we import the module

# in this way, we need to explicitly mention the module name before calling the method
import ex_module
ex_module.method()

# here is how we call the method without mentioning the module name
# inorder to make all the methods to be imported this way, just say
# from ex_module import *

from ex_module import method
method()