import sys
import math


def paint_calc(height, width, cover):
    """
        Calculate how many cans of paint are required to paint an area of 
        height x width sqaure meters, given that 1 can can cover sqm_per_can
        square meters.
    """
    try:
        area = height * width
        cans = math.ceil(area / cover)
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    
    return cans

try:
    height = float(sys.argv[1])
    width = float(sys.argv[2])
    cover = float(sys.argv[3])
    cans = paint_calc(width=width, height=height, cover=cover)
    print("{} can(s) of paint are required to cover {} x {} square meters".format(cans, height, width))
except ValueError:
    print("Only numerical values are allowed")
except UnboundLocalError:
    pass
