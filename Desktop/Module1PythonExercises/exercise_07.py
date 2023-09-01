#Sushmita Hari
quitList = []
evenList = []
quit = input("Enter a number or QUIT to quit: ")
while quit != "QUIT":
    quitNumber = int(quit)
    quitList.append(quitNumber)
    quit = input("Enter a number or QUIT to quit: ")
print("All Nums: ", quitList)
for i in range(len(quitList)):
    if quitList[i]%2 == 0:
        evenList.append(quitList[i])
print("Even Nums: ", evenList)