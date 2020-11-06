def task3(num1, num2):
    if num1 == 65 or num2 == 65 or num1 + num2 == 65:
        return True
    else:
        return False


#test
print(task3(65,72))
print(task3(5,65))
print(task3(5,60))
print(task3(5,62))
print(task3(5,35))
