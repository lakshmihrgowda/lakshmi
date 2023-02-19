#4.    Create a class named ‘Shape’ with a method to print 
#“This is this shape”. Then create two others classes named
#‘Rectangle’, ‘Circle’ inheriting the shape class, both having 
#the method to print “This is rectangular shape” and 
#“This is circular shape” respectively.
#Or
#Create a subclass ‘Square’ of ‘Rectangle’ having a method to print 
#“square is a rectangle”. Now call the method of ‘Shape’ and 
#‘Rectangle’ class by the object of ‘Square’ class.
class Shape():
    def m(self):
        print("This is Shape")  
class Rectangle(Shape):
    def m1(self):
        print("This is rectangular shape")
class Circle(Shape):
    def m2(self):
        print("This is circular shape")
sp = Shape()       
r = Rectangle()  
c = Circle()  
sp.m() 
r.m1()
c.m2()
 
