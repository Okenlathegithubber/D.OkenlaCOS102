# You have been given the task to apply your algorithmic skills in implementation strategy to solving this problem. 
# Your task is to generate the algorithm and python program to represent the data in a tabular form.

# Ask user how many students there are in class.
students_num = int(input("How many students are in the class? "))

# A list to save the information of the students.
student_info = []

# To put in the in the information of each student.
for i in range(students_num):
    gender = input(f"Is Student {i+1} male or female? ")
    if gender == "male" or gender == "Male":
        male_students = []
        name = input(f"Enter the name of the student {i+1}: ")
        age = input(f"Enter the age of the student {i+1}: ")
        height = input(f"Enter the height (cm) of the student {i+1}: ")
        score = input(f"Enter the score of the student {i+1}: ")
        print("")
        male_students.append((name, age, height, score))
    elif gender == "female" or gender == "Female":
        female_students = []
        name = input(f"Enter the name of the student {i+1}: ")
        age = input(f"Enter the age of the student {i+1}: ")
        height = input(f"Enter the height (cm) of the student {i+1}: ")
        score = input(f"Enter the score of the student {i+1}: ")
        print("")
        female_students.append((name, age, height, score))
    else:
        print("Please enter male or female.")

# To print out a table for the student information.
print("{:<15}".format("Table for Male Students"))
print("{:<15}{:<15}{:<15}{:<15}".format("Name", "Age", "Height", "Score"))
for row in male_students:
    print("{:<15}{:<15}{:<15}{:<15}".format(row[0], row[1], row[2], row[3]))

print("{:<15}".format("Table for Female Students"))
print("{:<15}{:<15}{:<15}{:<15}".format("Name", "Age", "Height", "Score"))
for row in female_students:
    print("{:<15}{:<15}{:<15}{:<15}".format(row[0], row[1], row[2], row[3]))

