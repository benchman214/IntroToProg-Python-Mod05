# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   NDeAsis, 3/2/2025, Revised Script
#   NDeAsis, 3/3/2025, Revised Script
# ------------------------------------------------------------------------------------------ #
import json
import io as _io

# Constants
FILE_NAME: str = 'MyLabData.json'

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Variables and constants
student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
student_data: list = []
students: list = []
csv_data: str = ''
file = None
menu_choice: str


# Read the file data into a table
# Extract the data
file = open(FILE_NAME, "r")
for row in file.readlines():
    # Transform the data
    student_data = row.split(',')
    student_data = []
    # Load it into collection (list of lists)
    students.append(student_data)
file.close()

# Present and Process the data
while True:

    # Menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input
    if menu_choice == "1":
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        student_data = [student_first_name,student_last_name,course_name]
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process and create / display a message
        print("-"*50)
        for student in students:
            print(f"Student {student_first_name} {student_last_name} is enrolled in {course_name}")
        print("-"*50)
        continue

    # Save
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        for student in students:
            csv_data = f"{student[0]},{student[1]},{student[2]}\n"
            file.write(csv_data)
        file.close()
        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student[0]} {student[1]} is enrolled in {course_name}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
