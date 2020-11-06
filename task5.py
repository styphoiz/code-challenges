import math
def triangle_area(num1,num2,num3):
    sides = 1/2 * (num1 + num2 + num3)
    area = math.sqrt(sides*(sides-num1)*(sides-num2)*(sides-num3))
    return area

#test
print(triangle_area(3,4,5))
print(triangle_area(6,6,6))
