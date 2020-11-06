def fah_cel(num):
    return (num - 32) * 5/9
def cel_fah(num):
    return num * (9/5) + 32

#test
print(cel_fah(-10))
print(fah_cel(14))