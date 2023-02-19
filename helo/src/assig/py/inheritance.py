#2.    Create a class with a method prints “This is a parent class” and 
#its sub-class with another method prints “This is a child class”. 
#Now, create and object for child class of the class and call.
#a-method of parent class by object of parent
#b-method of child class by object of child
#c-method of parent class by object of child
class parent:
    c = 10    
    def __init__(self, c):    
        print("this is a parent class")
class child(parent):
    def __init__(self, d):
        d=20
        print("this is a child class")
a = parent()
a.display()
b = child()
b.display()
