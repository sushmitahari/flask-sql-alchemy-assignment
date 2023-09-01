#Sushmita Hari
#I used code from the website Fav Tutor to create a function that turns a list into one string
#https://favtutor.com/blogs/list-to-string-python
def listtoString(s):
    #This creates the function
    string = " "
    #This makes sure the string has spaces
    return string.join(s)
    #This uses the join method that concatenates all of the strings from the list and turns it into one string
wordList = []
for i in range(5):
    word = input("Enter a word: ")
    wordList.append(word)
print("Words: ", wordList)
print("One String: ", listtoString(wordList))