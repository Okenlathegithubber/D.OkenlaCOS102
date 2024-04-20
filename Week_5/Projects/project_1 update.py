# Tkinter Application Project

# This project is designed to sign in any members of GIG logistics and welcome them to the app.

from tkinter import *  
from tkinter import messagebox

employees = {
        "ADENIRAN Oluwatamilore" : "Logistics",
        "ADEWUMI Ayomide" : "Accounting",
        "ADOH-AJAGBE Oshim" : "Delivery",
        "AGBAKURU-NWOGU Chukwunonye" : "Accounting",
        "AGBAKWURU Chiemeziem" : "Logistics",
        "AKINDE Oluwatimehin" : "Accounting",
        "ARNIKA Osose" : "Logistics",
        "ATELLY Daniel" : "Delivery",
        "AZOGU Onyekachi" : "Delivery",
        "BETURE Shalom" : "Delivery",
        "CHUKWUMA Nedi" : "Logistics",
        "EBI Stephanie" : "Accounting",
        "EGBORO Jason" : "Administration",
        "EJEDIMU Edward" : "Delivery",
        "ELERI Otu" : "Administration",
        "EZE Onyinyechi" : "Administration",
        "EZEONYE Makouchukwu" : "Logistics",
        "GIWA Moyosore" : "Logistics",
        "ICHA Ayonete" : "Accounting",
        "IKPATI Eche" : "Accounting",
        "ILOENYOSI Michael" : "Delivery",
        "IYAWE Oluwadamilola" : "Delivery",
        "NWOKOLO Chijindu" : "Logistics",
        "NWOTOKUBO Joseph" : "Logistics",
        "OBASOGIE Daisy" : "Accounting",
        "OBI Samuel" : "Accounting",
        "OBIALOR Betha" : "Accounting",
        "OGBONNA Boluwatife" : "Delivery",
        "OIGBOCHIE Mary" : "Delivery",
        "OKOCHA-OJEAH Raphael" : "Administration",
        "OKOLO Victor" : "Administration",
        "OKORO Derek" : "Logistics",
        "OLOWOKERE Akorede" : "Accounting",
        "OLUBUADE Rasheed" : "Accounting",
        "OSEMEKE Daniel" : "Accounting",
        "OSSAI Mary-Cynthia" : "Logistics",
        "PETER Owoede" : "Logistics",
        "QUADRI Oluwafikunmi" : "Delivery",
        "UDE-IBE Uchenna" : "Delivery",
        "UMEH Ejike" : "Administration"
    }

def welcomeMessage(username, users):
    # Create a Tkinter window
    window = Toplevel(root)
    window.title("Sign-in Successful")
    window.geometry("900x500")

    label_1 = Label(window, text=f"Welcome back {username}\n")
    label_1.pack()
    label_2 = Label(window, text="Sign-in Successful!!!")
    label_2.pack()
    label_3 = Label(window, text=f"Other users in the same department: \n")
    label_3.pack()
    for employees in users:
        label_4 = Label(window, text=f"{employees}\n")
        label_4.pack(padx = 20)

    close_button = Button(window, text="Close", command=window.destroy)
    close_button.pack()

    # Run the Tkinter event Loop
    root.mainloop()

# Function to check if the user can sign-in.
def sign_in():
    username = username_entry.get()
    department = department_entry.get()
    
    same_dept = []
    for name, dept in employees.items():
        if dept == department and name != username:
            same_dept.append(name)

    if username in employees and employees[username] == department:
        welcomeMessage(username, same_dept)
    else:
        messagebox.showerror("Login", "Invalid username or department")

# Function called when the user clicks the close button.
def close_button_click():
    #print("Button clicked!")

    #  Ask for user confirmation
    result = messagebox.askyesno("Confirmation", "Are you sure you want to close the page?")
    if result == True:
        # Close the window
        root.destroy()
    else:
        # Do nothing
        pass

# Create main window
root = Tk()
root.title("Login Form")
root.geometry("500x250")

# Create username Label and entry
username_label = Label(root, text="Username:")
username_label.pack()
username_entry = Entry(root)
username_entry.pack()

# Create department Label and entry
department_label = Label(root, text="Department:")
department_label.pack()
department_entry = Entry(root)
department_entry.pack()

# Create Sign-in button
login_button = Button(root, text="Sign-in", command=sign_in)
login_button.pack(pady= 20)

# Create Close button
close_button = Button(root, text="Close", command=close_button_click)
close_button.pack()

# Run the main event Loop
root.mainloop()