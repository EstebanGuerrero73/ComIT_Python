""" A survey was carried out to 15 students in a University where the following 
information was requested: Photo ID #, SEX, SALARY, JOB.
 • PHOTO ID # (It's an integer)
 • SEX (1 - Male 2 - Female)
 • JOB (1 - If you work 2 - Do not work)
 • SALARY (An integer value)
Write the algorithm that allows reading and storing the requested data 
in vectors, then calculate and print:
 • Percentage of men in the university
 • Percentage of women in the university
 • Percentage of men who work and average salary
 • Percentage of working women and average salary """

print("\n\n    ***   SURVEY   ***\n\n")

students_num = int(input("\nPlease enter the number of students: "))
students = [[0 for col in range(4)] for row in range(students_num)]

for row in range(students_num):
    students[row][0]=int(input(f"\nPlease enter the photo ID # of the student number {row+1}: "))
    students[row][1]=int(input(f"\nPlease enter the sex of the student number {row+1} (1-Male   2-Female): "))
    students[row][2]=int(input(f"\nPlease indicate if the student number {row+1} have a job (1-Yes   2-No): "))
    students[row][3]=float(input(f"\nPlease the salary of the student number {row+1}: "))

print("\n\nPHOTO ID      SEX         JOB      SALARY[$]\n\n")

for row in range(students_num):
    
    if students[row][1] == 1:
        sex = "Male"
    else:
        sex = "Female"

    if students[row][2] == 1:
        work = "Yes"
    else:
        work = "No"    

    print(f"{students[row][0]}            {sex}            {work}            {students[row][3]}\n")

men, women, men_working, women_working, men_salary, women_salary = 0, 0, 0, 0, 0, 0
for row in range(students_num):

    if students[row][1] == 1:
        men += 1
    else:
        women += 1

    if (students[row][1] == 1) and (students[row][2] ==1):
        men_working += 1
        men_salary += students[row][3]

    if (students[row][1] == 2) and (students[row][2] ==1):
        women_working += 1
        women_salary += students[row][3]

print("    ***   STATS   ***\n\n")

print(f"\nPercentage of men in the university = {men/students_num*100} %")
print(f"\nPercentage of women in the university = {women/students_num*100} %")

if men == 0:
    print(f"\nPercentage of men who work = There were no men in the survey")
    print(f"\nAverage salary of men = There were no men in the survey")
else:
    print(f"\nPercentage of men who work = {men_working/men*100} %")

if men_working == 0:
    print(f"\nAverage salary of men = None of the men in the survey are working")
else:
    print(f"\nAverage salary of men = {men_salary/men_working} %")

if women == 0:
    print(f"\nPercentage of women who work = There were no women in the survey")
    print(f"\nAverage salary of women = There were no women in the survey")
else:
    print(f"\nPercentage of women who work = {women_working/women*100} %")

if women_working == 0:
    print(f"\nAverage salary of women = None of the women in the survey are working")
else:
    print(f"\nAverage salary of women = {women_salary/women_working}  %")

input("\n\nPress Enter to exit")
