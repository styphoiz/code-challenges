def print_vowel(text):
    output = ""
    for s in text:
        if(s=="a"or s=="e"or s=="i"or s=="o"or s=="u"or s=="A"or s=="E"or s=="I"or s=="O"or s=="U"):
            print(s)
            if(output==""):
                output = s
            else:
                output += " " + s
    return output

print(print_vowel("HellO, this Is a vowEl test to identify >> A a E e I i O o U u"))

