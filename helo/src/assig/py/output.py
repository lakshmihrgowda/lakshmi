#15.    Write a program to display below Output:
#a)    1 
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
#b)    1
#2 2
#3 3 3 
#4 4 4 4 
#5 5 5 5 5
#c)    5 5 5 5 5 
#4 4 4 4 
#3 3 3 
#2 2 
#1
#d)    5 4 3 2 1
#4 3 2 1
#3 2 1 
#2 1
#1



rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
    
rows = 5
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')
    
rows = 5
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print(" ")
    
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()