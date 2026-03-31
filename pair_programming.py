# Mikah Plitt
# Pair Programming
# Function Prompt 2 - Change coordinates from polar to Cartesian

import math
def polar_to_cartesian(r, theta): 
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

#Madison's Commentary:
#There are not any comments on the function, but it is also a pretty short/simple function.
#The function accepts polar coordinates in radius and angle theta, then uses the math import
#and the algebraic equations for converting to cartesian coordinates to convert the given values
#into x and y values.