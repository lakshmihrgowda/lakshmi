class emp:
    def hello_emp(self,e_name=None):
        if e_name is not None:
            print("Hello",e_name)
        else:
            print("Hello")
emp1=emp()
emp1.hello_emp()
emp1.hello_emp("Kiran")



class Overloading:#Overload@signature()
    def getMethod(self,j):
        print("First method",j)#getMethod.overload@signature(“int”)
    def getMethod(self,i):
        print("Second method",i)
obj = Overloading()
obj.getMethod(1)
obj.getMethod(2)

