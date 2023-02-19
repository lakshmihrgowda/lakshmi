#7.    Write a program for addition, subtraction, multiplication, division and modulus. By using nested if.
num1 = int(input("enter value"))
num2 = int(input("enter value"))
ch = input("enter the operation + add,- sub,* mul,/ div,% mod,:")
result = 0
if ch == '+' :
    result = num1 + num2
    print(num1, ch , num2, ":", result)
elif ch == '-' :
    sub = num1 - num2
    print(num1, ch , num2, ":", sub)
elif ch == '*' :
    result = num1 * num2
    print(num1, ch , num2, ":", result)
elif ch == '/' :
    result = num1 / num2
    print(num1, ch , num2, ":", result)
elif ch == '%' :
    result = num1 % num2
    print(num1, ch , num2, ":", result)
else:
    print("Input character is not recognized!")
                        