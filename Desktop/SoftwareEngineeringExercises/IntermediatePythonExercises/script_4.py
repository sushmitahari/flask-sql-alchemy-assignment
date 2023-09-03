sum = 0
for i in range(5):
    while True:
        try:
            print("Enter int #", i+1, ":")
            integerNumber = input()
            totalNumber = int(integerNumber)
            sum+=totalNumber
            break
        except ValueError:
            print("Invalid input. Please enter an int.")
print("Your sum is ", sum)