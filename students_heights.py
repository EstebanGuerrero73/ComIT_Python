""" Write a program that allows you to enter the height of 10 students, 
 then show the average height, and how many elements are above average, 
 how many are below average.
 """
def students_weight_stats(students_num):

    heights = list()
    above = 0
    below = 0
    on_avrg = 0

    for index in range(students_num):
        height = float(input(f"\nPlease enter the height (cm) of the student {index + 1}: "))
        heights.insert(index, height)

    total = sum(heights)
    average = total / students_num

    for height in heights:
        if height > average:
            above += 1
        if height < average:
            below += 1
        if height == average:
            on_avrg +=1

    return [total, average, above, below, on_avrg]
    
students_num = int(input("\nPlease enter the number of students: "))
stats = students_weight_stats(students_num)
print(f"\nThe total height of the {students_num} students is {stats[0]} cm")
print(f"\nThe average height of the {students_num} students is {stats[1]} cm")
print(f"\nThere are {stats[2]} students above average height")
print(f"\nThere are {stats[3]} students below average height")
print(f"\nThere are {stats[4]} students with the average height")
input("\nPress Enter to exit")