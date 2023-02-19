class add:  
    def __init__(self, a, b):  
        self.a = 10  
        self.b = 20  
  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
  
  
emp1 = Employee("Vinay", 101)  
emp2 = Employee("Metha", 102)  
  
# accessing display() method to print employee 1 information  
  
emp1.display()  
  
# accessing display() method to print employee 2 information  
emp2.display()
