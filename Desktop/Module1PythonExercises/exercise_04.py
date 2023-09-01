#Sushmita Hari
#I used code from a website called Spark By Examples in order to figure out how to find the average in the list of floats
#https://sparkbyexamples.com/python/average-of-list-in-python/
number = input("Enter a number: ")
listNumber = int(number)
floatList = []
for n in range(listNumber):
    print("Enter number", n+1, ":")
    floatNumber = input()
    floatListNumber = float(floatNumber)
    floatList.append(floatListNumber)
print("List: ", floatList)
#These two variables initialize the sum and the initial start of the while loop
total = 0
i = 0
#While i is less than the length of the list of floats
while (i < len(floatList)):
    #In the loop, it adds each number from the list of floats into the total
    total = total +floatList[i]
    #As it goes down each index number, the index number increases as each one is added to the total
    i = i + 1
#This prints out how to find the average
print("Average: ", total/len(floatList))