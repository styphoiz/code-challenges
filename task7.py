def fahrenheit_to_celsius(num):
    return (num - 32) * 5/9
def celsius_to_fahrenheit(num):
    return num * (9/5) + 32

#test
print(celsius_to_fahrenheit(-10))
print(fahrenheit_to_celsius(14))