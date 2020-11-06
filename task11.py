def compare(str1, str2):
    output = ""
    for s in str1:
        for s2 in str2:
            if s == s2:
                if output == "":
                   output = s
                else:
                    output += ", " + s
    return "Common letters: " + output
print(compare("house","computers"))