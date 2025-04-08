# program to calculate cirle area and circumference 

import numpy as np

radius = float(input("Enter the radius of the circle in cm: "))
area = np.pi*radius**2
circumference = 2*np.pi*radius

print(f"the circle of radius {radius} cm has an area of {area:.2f} cm², and a circumference of {circumference:.2f} cm")
