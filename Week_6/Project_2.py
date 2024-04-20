# Python Project to that tells a person if they are admitted into computer science or mass communication using GUI.
# To enter computer science, score 250 and above in jamb, have at least 5 credits in key subjects and pass an interview

from tkinter import *
from tkinter import messagebox

# List to put in candidates information.
admitted = []
not_admitted = []

# Function to show list of admitted candidates.
def show_admitted():
    new_window = Tk()
    new_window.title("Admitted Candidates")
    new_window.geometry("500x300")
    bg_colour = "lightblue"
    new_window.configure(bg=bg_colour) 

    admitted_label = Label(new_window,text="Admitted Candidates:",bg=bg_colour)
    admitted_label.pack()
    for detail in admitted:
        candidates_label = Label(new_window,text=detail, bg=bg_colour)
        candidates_label.pack()

    close_button = Button(new_window, text="Close", command=new_window.destroy, bg="orangered")
    close_button.pack(pady=10)

# Function to show list of non-admitted candidates.
def show_not_admitted():
    new_window = Tk()
    new_window.title("Admitted Candidates")
    new_window.geometry("500x200")
    bg_colour = "lightblue"
    new_window.configure(bg=bg_colour) 

    not_admitted_label = Label(new_window,text="Non-Admitted Candidates:",bg=bg_colour)
    not_admitted_label.pack()
    for detail in not_admitted:
        candidates_label = Label(new_window,text=detail,bg=bg_colour)
        candidates_label.pack()
    
    close_button = Button(new_window, text="Close", command=new_window.destroy, bg="orangered")
    close_button.pack(pady=10)

# Function for submitting computer science candidate information.
def submit_compsci():
    name = name_entry.get()
    math = math_entry.get()
    eng = eng_entry.get()
    phy = phy_entry.get()
    csc = csc_entry.get()
    dp = dp_entry.get()

    grade = ["A", "B", "C"]

    if jamb_score_cs >= 250 and interview == "Y" and math and eng and phy and csc and dp in grade:
        messagebox.showinfo("Processs Complete","Congratulations, You have been admitted into the Computer Science program.")
        admitted.append(name)

    else:
        messagebox.showinfo("Processs Complete","Unfortunately, You have not been admitted in to the Computer Science program.")
        not_admitted.append(name)
    
    window.destroy()

# Function for submitting mass communication candidate information.
def submit_masscom():
    name = name_entry.get()
    math = math_entry.get()
    eng = eng_entry.get()
    gov = gov_entry.get()
    his = his_entry.get()
    lit_in_eng = lit_in_eng_entry.get()

    grade = ["A", "B", "C"]

    if jamb_score_mc >= 230 and interview == "Y" and math and eng and gov and his and lit_in_eng in grade:
        messagebox.showinfo("Processs Complete","Congratulations, You have been admitted into the Mass Communication program.")
        admitted.append(name)
        
    else:
        messagebox.showinfo("Processs Complete","Unfortunately, You have not been admitted in to the Mass Communication program.")
        not_admitted.append(name)

    window.destroy()

# Function to check if the admission criteria are met.
def check_compsci_admission():
    global window

    window = Tk()
    window.title("Computer Science Admission Process")
    window.geometry("500x500")
    bg_colour = "lightblue"
    window.configure(bg=bg_colour) 

    global math_entry

    math_label = Label(window, text="What was your Grade in Mathematics (WAEC):", bg=bg_colour)
    math_label.pack()
    math_entry = Entry(window)
    math_entry.pack()

    global eng_entry

    eng_label = Label(window, text="What was your Grade in English (WAEC):", bg=bg_colour)
    eng_label.pack()
    eng_entry = Entry(window)
    eng_entry.pack()

    global phy_entry

    phy_label = Label(window, text="What was your Grade in Physics (WAEC):", bg=bg_colour)
    phy_label.pack()
    phy_entry = Entry(window)
    phy_entry.pack()

    global csc_entry

    csc_label = Label(window, text="What was your Grade in Computer Studies (WAEC):", bg=bg_colour)
    csc_label.pack()
    csc_entry = Entry(window)
    csc_entry.pack()

    global dp_entry

    dp_label = Label(window, text="What was your Grade in Data Processing (WAEC):", bg=bg_colour)
    dp_label.pack()
    dp_entry = Entry(window)
    dp_entry.pack()

    submit_button = Button(window, text="Submit", command=submit_compsci, bg="lightgreen")
    submit_button.pack(pady=10)

    close_button = Button(window, text="Close", command=window.destroy, bg="orangered")
    close_button.pack(pady=10) 

    global jamb_score_cs
    global interview

    jamb_score_cs = int(jamb_score_entry.get())
    interview = interview_entry.get()

# Function to check if admission criteria are met.
def check_masscom_admission():
    global window

    window = Tk()
    window.title("Mass Communication Admission Process")
    window.geometry("500x500")
    bg_colour = "lightblue"
    window.configure(bg=bg_colour) 

    global math_entry

    math_label = Label(window, text="What was your Grade in Mathematics (WAEC):", bg=bg_colour)
    math_label.pack()
    math_entry = Entry(window)
    math_entry.pack()

    global eng_entry

    eng_label = Label(window, text="What was your Grade in English (WAEC):", bg=bg_colour)
    eng_label.pack()
    eng_entry = Entry(window)
    eng_entry.pack()

    global gov_entry

    gov_label = Label(window, text="What was your Grade in Government (WAEC):", bg=bg_colour)
    gov_label.pack()
    gov_entry = Entry(window)
    gov_entry.pack()

    global his_entry

    his_label = Label(window, text="What was your Grade in History (WAEC):", bg=bg_colour)
    his_label.pack()
    his_entry = Entry(window)
    his_entry.pack()

    global lit_in_eng_entry

    lit_in_eng_label = Label(window, text="What was your Grade in Literature-in-English (WAEC):", bg=bg_colour)
    lit_in_eng_label.pack()
    lit_in_eng_entry = Entry(window)
    lit_in_eng_entry.pack()

    submit_button = Button(window, text="Submit", command=submit_masscom, bg="lightgreen")
    submit_button.pack(pady = 10)

    close_button = Button(window, text="Close", command=window.destroy, bg="orangered")
    close_button.pack(pady=10)

    global jamb_score_mc
    global interview

    jamb_score_mc = int(jamb_score_entry.get())
    interview = interview_entry.get()

# Function to reset the enteries.
def reset():
    name_entry.delete(0, END)
    jamb_score_entry.delete(0, END)
    interview_entry.delete(0, END)

# To create am interface
root = Tk()
root.title("PAU Admission Center")
root.geometry("500x700")
bg_colour = "lightblue"
root.configure(bg=bg_colour) 

# To create Name label and entry
name_label = Label(root, text="Enter Candidate Name:", bg=bg_colour)
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

# To create Jamb score label and entry
jamb_score_label = Label(root, text="Enter Jamb Score:", bg=bg_colour)
jamb_score_label.pack()
jamb_score_entry = Entry(root)
jamb_score_entry.pack()

# To create Interview label and entry
interview_label = Label(root, text="Did you pass Interview: (Y/N):", bg=bg_colour)
interview_label.pack()
interview_entry = Entry(root)
interview_entry.pack()

# Clear Button. To clear entries in a gui window
reset_button = Button(root, text="Reset", command=reset, bg="cyan")
reset_button.pack(ipady=10, ipadx=40, pady=20)

# To create admission button for Computer Science and Mass Communication.
compsci_admission_button = Button(root, text="Computer Science Admissions", command=check_compsci_admission, bg="lightgreen")
compsci_admission_button.pack(pady= 20)

masscom_admission_button = Button(root, text="Mass Communication Admissions", command=check_masscom_admission, bg="lightgreen")
masscom_admission_button.pack(pady=20)

# Button to show admitted and non-admitted candidates.
admitted_button = Button(root, text="Admitted Candidates", command=show_admitted, bg="yellow")
admitted_button.pack(pady=20)
not_admitted_button = Button(root, text="Non-Admitted Candidates", command=show_not_admitted, bg="yellow")
not_admitted_button.pack(pady=20)

# Button to close the application.
close_button = Button(root, text="Close", command=root.destroy, bg="orangered")
close_button.pack(ipady=10,ipadx=10, pady=20)

# Run the main event Loop
root.mainloop()