class add:    
    def add (self, a, b): 
        return a+b 
        
   
cobj = add()
print("Enter Two Numbers: ", end="")
One = int(input())
Two = int(input())

res = cobj.add(One, Two)

print("\n" +str(One)+ " + " +str(Two)+ " = " +str(res))