#5.    Write a program to find area of rectangle.
def area_of_rectangle(width,height):
    Area = width * height
    Perimeter = 2 * (width + height)
    print("Area of a rectangle is: %.2f" %Area)
    print("Perimeter of rectangle is: %.2f" %Perimeter)
width = float(input('Enter the width of a rectangle: '))
height = float(input('Enter the height of a rectangle: '))
area_of_rectangle(width,height)