# print("Welcome to the Admission Office!")

# student_num = int(input("How many students are applying for a program >> "))


# for i in range(student_num):

#     program = int(input("Programs available for application: \n1. Computer Science, \n2. Mass Communication \nWhat program are you applying for? >> "))

#     admitted = []
#     not_admitted = []

#     if program == 1:
#         name = input("What is your name >> ")
#         jamb_score = int(input("What was your score in jamb >> "))
#         subjects = ["Mathematics", "English Language", "Physics", "Computer Studies", "Data Processing"]
#         interview = input("Did you pass the interview? (Y/N)>> ")
#         letter_score = ["A", "B", "C"]

#         for s in subjects:
#             score = input(f"Enter Letter Grade for {s} >> ")

#         if jamb_score >= 250 and score in letter_score and interview == "Y" or interview == "y":
#             admitted.append(name)
#         else: 
#             not_admitted.append(name)
    
#     if program == 2:
#         name = input("What is your name >> ")
#         jamb_score = int(input("What was your score in jamb >> "))
#         subjects = ["Mathematics", "English Language", "Government", "History", "Literature-in-English"]
#         interview = input("Did you pass the interview? (Y/N) >> ")

#         for s in subjects:
#             score = input(f"Enter Letter Grade for {s} >> ")

#         if jamb_score >= 230 and score in letter_score and interview == "Y" or interview == "y":
#             admitted.append(name)
#         else:
#             not_admitted.append(name)
# print(admitted)
# print(not_admitted)

from tkinter import *

root = Tk()
root.title("Purchase Form")
root.geometry("500x250")

btn = Button(root, text = 'Click me !', command = root.destroy)

btn.pack(side=LEFT, padx=15, pady=20)
root.mainloop()
