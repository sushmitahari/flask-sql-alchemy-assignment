#Sushmita Hari
stringInput = input("Enter a string: ")
stringList = []
charList = []
for i in range(len(stringInput)):
    stringList.append(stringInput[i])
for j in range(len(stringList)):
    charList.append(stringList[j:j+3])
print(charList)