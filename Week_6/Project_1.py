# A Python project that charges people based on their location and weight of their package in a GUI format.

from tkinter import *  
from tkinter import messagebox

def check_price():
    location = location_entry.get()
    weight = weight_entry.get()
    weight_int = int(weight)
    if location == "Ibeju-Lekki" and weight_int >= 10:
        messagebox.showinfo("Price", "Your Price is N5,000")
        messagebox.askyesno("Confirm", "Do you want to Deliver?")
        if True:
            messagebox.showinfo("Successful", "Delivery successfully")
        else:
            pass

    elif location == "Ibeju-Lekki" and weight_int < 10:
        messagebox.showinfo("Price", "Your Price is N3,500")
        messagebox.askyesno("Confirm", "Do you want to deliver?")
        if confirm == True:
            messagebox.showinfo("Successful", "Deliver successfully")
        else:
            pass

    elif location == "Epe" and weight_int >= 10:
        messagebox.showinfo("Price", "Your Price is N10,000")
        confirm = messagebox.askyesno("Confirm", "Do you want to deliver?")
        if confirm == True:
            messagebox.showinfo("Successful", "Order successfully")
        else:
            pass


    elif location == "Epe" and weight_int < 10:
        messagebox.showinfo("Price", "Your Price is N5,000")
        messagebox.askyesno("Confirm", "Do you want to deliver?")
        if confirm == True:
            messagebox.showinfo("Successful", "Delivery successfully")
        else:
            pass

    else:
        messagebox.showwarning("Location Error", "Location cannot be delivered to.")

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
root.title("Purchase Form")
root.geometry("500x250")

# welcomelabel = Label(root, "Welcome to Simi Services !!!")
# welcomelabel.pack()

# Create location Label and entry
location_label = Label(root, text="Enter Location to Deliver:")
location_label.pack()
location_entry = Entry(root)
location_entry.pack()

# Create weight Label and entry
weight_label = Label(root, text="Enter Weight of Package to be Delivered:")
weight_label.pack()
weight_entry = Entry(root)
weight_entry.pack()

# Create Submit button
submit_button = Button(root, text="Submit", command=check_price)
submit_button.pack()

# Create Close button
close_button = Button(root, text="Close", command=close_button_click)
close_button.pack()

# Run the main event Loop
root.mainloop()
