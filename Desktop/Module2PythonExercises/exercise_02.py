string1 = input("Enter a string: ")
string2 = ""
string3 = ""
for i in string1:
    if (i.islower()):
        string2 +=i
    elif (i.isupper()):
        string3 +=i
string4 = string2 + string3
print(string4)