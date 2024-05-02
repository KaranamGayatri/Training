#Determine the grades of the class's students.
Score = int(input("Enter the student's score: "))
if Score >= 90:
    Grade = 'A'
elif Score >= 80:
    Grade = 'B'
elif Score >= 70:
    Grade = 'C'
elif Score >= 60:
    Grade = 'D'
else:
    Grade = 'F'

print("The student's score is: ",Score)
print("The student's grade is: ",Grade)