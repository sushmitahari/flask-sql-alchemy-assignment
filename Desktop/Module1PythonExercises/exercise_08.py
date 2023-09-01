#Sushmita Hari
numberList = []
numList = []
for i in range(10):
    print("Enter number: ", i+1, ":")
    number = input()
    listNumber = int(number)
    numberList.append(listNumber)
print("Original List: ", numberList)
for j in range(len(numberList)):
    if numberList.count(j) == 1:
        numList.append(j)
print("Nums that appear once: ", numList)