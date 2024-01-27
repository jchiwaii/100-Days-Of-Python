student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_value = 0
students = 0

for height in student_heights:
    sum_value += height

for student in student_heights:
    students += 1

average_height = round(sum_value/students)

print(average_height)
