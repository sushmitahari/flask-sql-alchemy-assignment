#Sushmita Hari
grade = input("Enter a grade from 0 to 100: ")
numberGrade = int(grade)
if (numberGrade <=100 and numberGrade >=90):
    print("Your grade is A")
elif (numberGrade <=89 and numberGrade>= 80):
    print("Your grade is B")
elif(numberGrade <=79 and numberGrade >= 70):
    print("Your grade is C")
elif(numberGrade <=69 and numberGrade>= 60):
    print("Your grade is D")
elif (numberGrade <=59 and numberGrade >=0):
    print("Your grade is F")
else:
    print("This value does not exist in the grading system")