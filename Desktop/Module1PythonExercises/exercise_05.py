#Sushmita Hari
#I looked at code from the website TutorialsPoint to understand and figure out the code for the common list
#https://www.tutorialspoint.com/python-program-to-find-common-elements-in-two-arrays
numberList = []
integerNumber = []
commonList = []
for i in range(5):
    number = input("Enter a number for the first list: ")
    listNumber = int(number)
    numberList.append(listNumber)
for n in range(5):
    intNumber = input("Enter a number for the second list: ")
    intListNumber = int(intNumber)
    integerNumber.append(intListNumber)
print("First List: ", numberList)
print("Second List: ", integerNumber)

for j in range(5):
    #If the index of the first and second list are not in the common list
    if numberList[j] in integerNumber and numberList[j] not in commonList:
        #This adds to the common list
        commonList.append(numberList[j])
    #If the index of the second and first list are not in the common list
    elif integerNumber[j] in numberList and integerNumber[j] not in commonList:
        #This adds to the common list
        commonList.append(integerNumber[j])
print("Common List: ", commonList)