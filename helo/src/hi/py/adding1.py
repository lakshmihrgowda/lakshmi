class add:
    def add(self, a, b):
        return a+b

print("Enter Two Numbers: ", end="")
One = int(input())
Two = int(input())

cobj = add()
res = cobj.add(One, Two)

print("\n" +str(One)+ " + " +str(Two)+ " = " +str(res))