# parabolic equation
import math

#### CHANGE THESE VALUES
r0 = 2 			# 2 mm (radius of quadrupole)
height = 1.8	# put height in mm
#### END OF CHANGING VALUES

x = math.sqrt((r0+height)**2 - r0**2)	
x_total_height =  x * 2 
# x = math.sqrt(y**2-r0**2)
print("x: ", x_total_height, "mm")
print("height: ", height, "mm")