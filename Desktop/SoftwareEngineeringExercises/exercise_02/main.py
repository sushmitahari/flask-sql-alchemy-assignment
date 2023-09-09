#Sushmita Hari
#I used the website GeeksforGeeks in order to figure out how to type the code for the Fibonacci sequence and a website called E Learning in order to learn how to import the random number generator in Python and how to use it
#https://www.geeksforgeeks.org/python-program-to-print-the-fibonacci-sequence/
#https://elearning.wsldp.com/python3/python-random-number-between-1-10/
import random
import time
def fibonacci(n):
    #If the number is less than 0, such as -1, or -2
    if n < 0:
        #Print "incorrect input"
        print("Incorrect input")
    #If the number is 0
    elif n == 0:
        #Return 0
        return 0
    #If the number is either 1 or 2
    elif n == 1 or n == 2:
        #Return 1, since 0+1 is 1
        return 1
    else:
        #For example, if the number is 17, this part adds the fibonacci sequence of number behind 17, which is 16, and the fibonacci sequence of the number 2 behind 16, which is 15
        return fibonacci(n-1) + fibonacci (n-2)
start_time = time.time()
#Using the randint function from the random import, I created a new variable called random_number that randomizes a number from 15 to 35
random_number = random.randint(15,36)
#This prints out the fibonacci sequence of any number from 15 to 35
print("fib(", random_number, ") =", fibonacci(random_number))
end_time = time.time()

elapsed_time = end_time - start_time
print("fib(", random_number, f") took {elapsed_time} seconds")


