#calculate area and perimeter of a rectangle 

height = float(input("Enter the height of the rectangle: "))
width = float(input("Enter the width of the rectangle: ")) 
area = height * width
perimeter = 2 * (height + width)

print(f"the area of the rectangle is {area:.2f} cm² and the perimeter is {perimeter:.2f} cm.")
