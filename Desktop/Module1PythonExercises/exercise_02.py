#Sushmita Hari
string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
if string1.endswith(string2) == True:
    print("True")
elif string2.endswith(string1) == True:
    print("True")
else:
    print("False")