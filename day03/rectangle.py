# calculate area and perimeter of a rectangle 

import sys

if len(sys.argv)<3:
  print("Usage: python rectangle.py <height_in_cm> <width_in_cm>")
  sys.exit(1)

try:
  height = float(sys.argv[1])
  width = float(sys.argv[2])
except ValueError:
  print("Please provide valid numbers for height and width")
  sys.exit(1)

area = height*width
perimeter = 2*(height + width)

print(f"the area of the rectangle is {area:.2f} cm² and the perimeter is {perimeter:.2f} cm.")
