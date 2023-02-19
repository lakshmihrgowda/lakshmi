#14.    Write a program to print the Multiplication table from 2 to 10.
number = int(input ("Enter the number of which the user wants to print the multiplication table: "))            
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
    print (number, 'x', count, '=', number * count)    
