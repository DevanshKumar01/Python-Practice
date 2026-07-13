#hypotenuse of a triangle

import math
a=float(input("enter side a: "))
b=float(input("enter side b: "))
hypotenuse = math.sqrt(a**2 + b**2)
print(f"the hypotenuse is: {round(hypotenuse , 2)}")