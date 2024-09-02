#Exercise: Student Grades Management System (GPT)
#Create a program that manages a list of student grades
#List c
Grades = list(('A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-'))

#Total number of grades. 
print('The total number of grades =', len(Grades))
#Type(Data) of list
print('The Data type of our list is:', type(Grades))
#First, Middle, and Last Grade
print('The first, middle, and last grade in our list are', Grades[0],Grades[4],Grades[8])

#Check if grade exists, print results
if 'B' in Grades:
    print('The grade \'b\' doesn\' exist.')

#Modify List
Grades[2] = ['A']
print('Our update grade:', Grades)
Grades[-3:] = ['D+', 'D', 'D-']
print('Grades after changing a range:', Grades)
Grades.insert(3,'B')
print('Updated grade at the 3rd index:', Grades)
Grades.append('E') 
print('Added grade to the end of our list', Grades)

#Extend list of grade w/ another list
FailingGrades = ['F']
Extended = Grades.extend(FailingGrades)
print('Grades after we \'ve appended another list to our Grades list:', Extended)
#Modify Lists continued. 
Grades.remove('D')
print('List after we removed a grade', Grades)
Grades.pop()
print('Updated grades after we\'ve removed the last grade:', Grades)
del Grades[0]
print('Grades after removing the first grade:', Grades)
Grades.clear()
print('Our Grades list after we\'ve cleared it:', Grades)

#Operator precedence 
Math = 9*7 + (14-5 / 3)
Math1 = (20/5) * 120 % 13
Math2 = (120*8 + 95%6) - 120

print('Result of 9*7 + (14-5 / 3)', Math)
print('Result of (20/5) * 120 % 13', Math1)
print('Result of (120*8 + 95%6) - 120', Math2)

