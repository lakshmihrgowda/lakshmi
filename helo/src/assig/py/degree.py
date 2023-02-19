#1.    Create a class ‘Degree’ having a method ‘getDegree’ that prints “I got a degree”.
#It has two subclasses namely ‘Undergraduate’ and ‘Postgraduate’ each having a method with 
#the same name that prints “I am a Undergraduate” and “I am a Postgraduate” respectively.
#Call the method by creating an object of each of the three classes.
class degree:
    name = "getdegree"
    def display(self):
        print("I got a degree")
class Undergraduate(degree):
    def display(self):
        print("I am a Undergraduate")
class Postgraduate(degree):
    def display(self):
        print("I am a Postgraduate")
deg = degree()
deg.display();
Ug = Undergraduate()
Ug.display(); 
Pg = Postgraduate()
Pg.display();    
