# calculate area and perimeter of a rectangle 

import sys

height = float(input("Enter the height of the rectangle in cm: "))
width = float(input("Enter the width of the rectangle in cm: ")) 
area = height*width
perimeter = 2*(height + width)

print(f"the area of the rectangle is {area:.2f} cm² and the perimeter is {perimeter:.2f} cm.")
