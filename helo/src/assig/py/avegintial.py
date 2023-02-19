#11.    Write a program to intalize a 5 subjects marks and find there average based on the average display grades:
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
average=(sub1+sub2+sub3+sub4+sub5)/5
if(average >= 75):
    print("Distinction")
elif(average >= 60 and average < 75):
    print("First Class")
elif(average >= 50 and average < 60):
    print("Second Class")
elif(average >= 35 and average < 50):
    print("Third Class")
else:
    print("Fail",average <= 35)
