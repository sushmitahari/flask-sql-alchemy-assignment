#Sushmita Hari
#I used code from a website called Tutorial Gateway in order to create a function that cubes a number
#https://www.tutorialgateway.org/python-program-to-calculate-cube-of-a-number/#google_vignette
def cube(n):
    #This multiplies each number from the argument n three times
    return n * n * n
integer = input("Enter a integer greater than 1: ")
cubedInteger = int(integer)
i = 0
while (i <= cubedInteger):
    cubed = cube(i)
    print("The cube of ", i, "is ", cubed)
    i = i + 1
