#Sushmita Hari
#I looked at the code from the website Soft Uni to figure out the code for the grid of 0s
#https://python-book.softuni.org/chapter-06-nested-loops.html
def grid():
    row = input("Enter a row num from 1 to 5: ")
    col = input("Enter a col num from 1 to 5: ")
    #In this nested for loop
    for i in range(5):
        for j in range(5):
            rowNumber = int(row)
            colNumber = int(col)
            #If the index number in the for loops represent the column and row number - 1
            if j == colNumber -1 and i == rowNumber -1:
                #It will print a one on the specific row and column and end with a space
                print("1 ", end = "")
            else:
                #It will print 0s on the rest of the grid and end with a space
                print("0 ", end = "")
        print()
grid()