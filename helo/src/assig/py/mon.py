#13.    Write a program to accept a number and display there year of the month.
def print_month_name(x):
    if (x==1):
        print ("Jan")
    if (x==2):
        print("Feb")
    if (x==3):
        print("March")
    if (x==4):
        print("April")
    if (x==5):
        print("May")
    if (x==6):
        print("June")
    if (x==7):
        print("July")
    if (x==8):
        print("August")
    if(x==9):
        print("September")
    if(x==10):
        print("October")
    if(x==11):
        print("November")
    if(x==12):
        print("December")
    if(x<1 or x>12):
        print("Invalid input")
month = int(input("Enter the month number: "))
print_month_name(month)