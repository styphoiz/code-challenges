def time(num):
    hour = num//60
    minute = num % 60
    if(hour>1):
        if(minute>1):
            return str(hour) + " hours, " + str(minute) + " minutes"
        else:
            return str(hour) + " hours, " + str(minute) + " minute"
    else:
            if(minute>1):
                return str(hour) + " hour, " + str(minute) + " minutes"
            else:
                return str(hour) + " hour, " + str(minute) + " minute"

#test
print(time(10))
print(time(100))
print(time(200))
print(time(61))
print(time(121))