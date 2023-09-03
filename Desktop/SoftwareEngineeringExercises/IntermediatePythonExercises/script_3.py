#Sushmita Hari
#I used the website Python For Beginners to figure out how to add the letters of the string to a dictionary
#https://www.pythonforbeginners.com/basics/create-a-dictionary-from-a-string-in-python
def string_to_dict(string2):
    dictionary = {}
    for i in string2:
        #I created this part of the code in order to figure out how to put the letters in lowercase and how to count the number of letters and spaces
        if i.isalpha():
            i = i.lower()
            #If the character is in the dictionary
            if i in dictionary:
                #This adds it to the dictionary
                dictionary[i]+=1
            else:
                #This assigns the index to the dictionary
                dictionary[i]=1
    #This returns the dictionary
    return dictionary
string1 = input("Enter a string: ")
stringToDictionary = string_to_dict(string1)
print(stringToDictionary)