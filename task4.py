def task4(num1,num2):
    if(num1 == 3 or num2 ==3):
        for i in str(int(num1 + num2)):
            if i=="3":
                return True
        return False
    else:
        return False

#tests
print(task4(3,5))
print(task4(3,10))
print(task4(13,10))
print(task4(20,3))


