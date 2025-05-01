# program to calculate cirle area and circumference 

import numpy as np
import sys 

if len(sys.argv)<2:
  print("Usage: python circle.py <radius_in_cm>")
  sys.exit(1)

try: 
  radius = float(sys.argv[1])
except ValueError: 
  print("Please provide a valid number for the radius")
  sys.exit(1)

area = np.pi*radius**2
circumference = 2*np.pi*radius

print(f"the circle has an area of {area:.2f} cm², and a circumference of {circumference:.2f} cm.")
