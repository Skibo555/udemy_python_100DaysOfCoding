# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total_height = 0
for height in student_heights:
  total_height = total_height + height
print("The total number of the student height is: {}".format(total_height))

number_of_students = 0
for student in student_heights:
  number_of_students = number_of_students + 1
print("The total number of student is: {}".format(number_of_students))

average_height = round(total_height/number_of_students)

print("The avarage height is: {}".format(average_height))