def print_vowel(text):
    output = ""
    for s in text:
        if(s.lower()=="a"or s.lower()=="e"or s.lower()=="i"or s.lower()=="o"or s.lower()=="u"):
            print(s)
            if(output==""):
                output = s
            else:
                output += " " + s
    return output

def print_vowel_alternate(text):
        vowels = "aeiou"
        output = ""
        for s in text:
            for v in vowels:
                if(s.lower()==v):
                    print(s)
                    if(output==""):
                        output = s
                    else:
                        output += " " + s
        return output


print(print_vowel("HellO, this Is a vowEl test to identify >> A a E e I i O o U u"))
print(print_vowel_alternate("HellO, this Is a vowEl test to identify >> A a E e I i O o U u"))

