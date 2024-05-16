# With your knowledge of Python GUI programming, design the algorithm and develop a 
# program that displays the menu for the food items available and takes orders from the
# customer.

from tkinter import *
from tkinter import messagebox,ttk
from PIL import Image, ImageTk

total_price_1 = 0
total_price_2 = 0
total_price_3 = 0
total_price_4 = 0
total_price_5 = 0

def display_menu():
    menu_window = Toplevel(root)
    menu_window.title("PAU Cafeteria Menu")
    menu_window.geometry("450x700")
    menu_window.config(bg="gold")
    image_path = "C:/Users/dvdok/Documents/D.OkenlaCOS102/Week_7/pau_logo.ico"
    menu_window.iconbitmap(image_path)

    # Assuming image.jpg is in the same directory as your script
    image_path = "C:/Users/dvdok/Documents/D.OkenlaCOS102/Week_7/CA_2 Menu.png"


    # # Open image file
    image = Image.open(image_path)
    
    # # Convert image to Tkinter-compatible format
    tk_image = ImageTk.PhotoImage(image)
    
    # # Create a label to display the image
    label = Label(menu_window, image=tk_image)
    label.image = tk_image
    label.pack(pady= 10)

    # Create a close button.
    close_button = Button(menu_window, text="Close", command=menu_window.destroy,bg="orangered")
    close_button.pack(pady=10)

def get_total_price(): 
    global total_price_1,total_price_2,total_price_3,total_price_4,total_price_5
    total_price = total_price_1 + total_price_2 + total_price_3 + total_price_4 + total_price_5
    discount = 0

    if 1000 <= total_price < 2500:
        discount_price = 0.1 * total_price
        discount = total_price - discount_price
    elif  2500 <= total_price < 5000:
        discount_price = 0.15 * total_price
        discount = total_price - discount_price
    elif total_price >= 5000:
        discount_price = 0.25 * total_price
        discount = total_price - discount_price
    elif total_price < 1000:
        discount_price = 0 * total_price
        discount = total_price - discount_price
        
    messagebox.showinfo("Total", f"Total Price is N{total_price}. \nDiscount is {discount_price}. \nNew Price is N{discount}")


def order_food():
    global total_price_1,total_price_2,total_price_3,total_price_4,total_price_5

    pasta_dic = {"Jollof Rice": 350,"Coconut Fried Rice": 350, "Jollof Spaghetti": 350}
    proteins_dic = {"Sweet Chili Chicken": 1100,"Grilled Chicken Wings": 400,"Fried Beef": 400,"Fried Fish": 500,"Boiled Egg": 200,"Sauteed Sausages": 200}
    side_dishes_dic = {"Savoury Beans":350,"Roasted Sweet Potatoes": 300,"Fried Plantains": 150,"Mixed Vegetable Salads": 150,"Boiled Yam": 150}
    beverages_dic = {"Water": 200,"Glass Drink (35cl)":150,"PET Drink (35cl)": 300,"PET Drink (50cl)": 300,"Glass/Canned Malt": 500,"Fresh Yo": 600,"Pineapple Juice": 350,"Mango Juice": 350,"Zobo Drinks": 350}
    soups_and_swallows_dic = {"Eba": 100,"Poundo Yam": 100,"Semo": 100,"Atama Soup": 450,"Egusi Soup": 480}

    if food == food_type_choice[0]:
        global total_price_1
        pasta_quantity = int(pasta_quantity_entry.get())
        selected_item = pasta.get()
        for key, value in pasta_dic.items():
            if selected_item in key:
                total_price_1 = value * pasta_quantity
              
    
    elif food == food_type_choice[1]:
        global total_price_2
        protein_quantity = int(protein_quantity_entry.get())  
        selected_item = proteins.get()
        for key, value in proteins_dic.items():
            if selected_item in key:
                total_price_2 = value * protein_quantity

    
    elif food == food_type_choice[2]:
        global total_price_3
        side_dish_quantity = int(side_dishes_quantity_entry.get())
        selected_item = side_dishes.get()
        for key, value in side_dishes_dic.items():
            if selected_item in key:
                total_price_3= value * side_dish_quantity
   

    elif food == food_type_choice[3]:
        global total_price_4
        beverage_quantity = int(beverages_quantity_entry.get())
        selected_item = beverages.get()
        for key, value in beverages_dic.items():
            if selected_item in key:
                total_price_4 = value * beverage_quantity
                


    elif food == food_type_choice[4]:
        soup_quantity = int(soups_and_swallows_quantity_entry.get())
        selected_item = soups_and_swallows.get()
        for key, value in soups_and_swallows_dic.items():
            if selected_item in key:
                global total_price_5
                total_price_5 = value * soup_quantity
                
    que = messagebox.askyesno("Order", "Do you still want to order?")
    if que == True:
        next_window.destroy()
        food_type.delete(0, END) 
        

    else:
        next_window.destroy()
        food_type.delete(0, END)
        tot_que = messagebox.askyesno("Order", "Do you want to show Total Price?")
        if tot_que == True:
            get_total_price()
        else:
            pass
        
                    
def next_page():
    global next_window
    next_window = Tk() 
    next_window.title("PAU Cafeteria")
    next_window.geometry("400x350")
    image_path = "C:/Users/dvdok/Documents/D.OkenlaCOS102/Week_7/pau_logo.ico"
    next_window.iconbitmap(image_path)
    next_window.config(bg=bg_colour)

    global food
    
    food = food_type.get()

    global pasta
    global pasta_quantity_entry
    global pasta_choice


    if food == food_type_choice[0]:
        pasta_label = Label(next_window,text="What do you want to Order: \n\nRice/Pasta:",font=20,bg=bg_colour)
        pasta_label.pack(pady=10)
        pasta_choice = ["Jollof Rice", "Coconut Fried Rice", "Jollof Spaghetti","None"]
        pasta = ttk.Combobox(next_window,values=pasta_choice)
        pasta.pack()

        pasta_quantity_label = Label(next_window,text="Quantity:",font=20,bg=bg_colour)
        pasta_quantity_label.pack(pady=10)
        pasta_quantity_entry = Entry(next_window)
        pasta_quantity_entry.pack()

    global proteins_choice
    global proteins
    global protein_quantity_entry

    if food == food_type_choice[1]:
        proteins_label = Label(next_window,text="What do you want to Order: \n\nProteins:",font=20,bg=bg_colour)
        proteins_label.pack(pady=10)
        proteins_choice = ["Sweet Chili Chicken","Grilled Chicken Wings","Fried Beef","Fried Fish","Boiled Egg","Sauteed Sausages","None"]
        proteins= ttk.Combobox(next_window,values=proteins_choice)
        proteins.pack()

        protein_quantity_label = Label(next_window,text="Quantity:",font=20,bg=bg_colour)
        protein_quantity_label.pack(pady=10)
        protein_quantity_entry = Entry(next_window)
        protein_quantity_entry.pack()

    global side_dishes_choice
    global side_dishes
    global side_dishes_quantity_entry

    if food == food_type_choice[2]:

        side_dishes_label = Label(next_window,text="What do you want to Order: \n\nSide Dishes:",font=20,bg=bg_colour)
        side_dishes_label.pack(pady=10)
        side_dishes_choice = ["Savoury Beans","Roasted Sweet Potatoes","Fried Plantains","Mixed Vegetable Salads","Boiled Yam","None"]
        side_dishes= ttk.Combobox(next_window,values=side_dishes_choice)
        side_dishes.pack()

        side_dishes_quantity_label = Label(next_window,text="Quantity:",font=20,bg=bg_colour)
        side_dishes_quantity_label.pack(pady=10)
        side_dishes_quantity_entry = Entry(next_window)
        side_dishes_quantity_entry.pack()

    global beverages_choice
    global beverages
    global beverages_quantity_entry

    if food == food_type_choice[3]:

        beverages_label = Label(next_window,text="What do you want to Order: \n\nBeverages:",font=20,bg=bg_colour)
        beverages_label.pack(pady=10)
        beverages_choice = ["Water","Glass Drink (35cl)","PET Drink (35cl)","PET Drink (50cl)","Glass/Canned Malt","Fresh Yo","Pineapple Juice","Mango Juice","Zobo Drinks","None"]
        beverages= ttk.Combobox(next_window,values=beverages_choice)
        beverages.pack()

        beverages_quantity_label = Label(next_window,text="Quantity:",font=20,bg=bg_colour)
        beverages_quantity_label.pack(pady=10)
        beverages_quantity_entry = Entry(next_window)
        beverages_quantity_entry.pack()
        
    global soups_and_swallows_choice
    global soups_and_swallows
    global soups_and_swallows_quantity_entry

    if food == food_type_choice[4]:
        soups_and_swallows_label = Label(next_window,text="What do you want to Order: \n\nSoups and Swallows:",font=20,bg=bg_colour)
        soups_and_swallows_label.pack(pady=10)
        soups_and_swallows_choice = ["Eba","Poundo Yam","Semo","Atama Soup","Egusi Soup","None"]
        soups_and_swallows = ttk.Combobox(next_window,values=soups_and_swallows_choice)
        soups_and_swallows.pack()

        soups_and_swallows_quantity_label = Label(next_window,text="Quantity:",font=20,bg=bg_colour)
        soups_and_swallows_quantity_label.pack(pady=10)
        soups_and_swallows_quantity_entry = Entry(next_window)
        soups_and_swallows_quantity_entry.pack()

    # Create order button
    order_button = Button(next_window,text="Order",command=order_food)
    order_button.pack(pady=10)

    # Create a close button.
    close_button = Button(next_window, text="Close", command=next_window.destroy,bg="orangered")
    close_button.pack(pady=10)



root = Tk()
root.title("PAU Cafeteria")
root.geometry("400x350")
image_path = "C:/Users/dvdok/Documents/D.OkenlaCOS102/Week_7/pau_logo.ico"
root.iconbitmap(image_path)
bg_colour = "cyan"
root.config(bg=bg_colour)

show_menu = Button(root,text="Show Menu",command=display_menu)
show_menu.pack()

name_label = Label(root,text="Name:",font=20,bg=bg_colour)
name_label.pack(pady=10)
name_entry = Entry(root)
name_entry.pack()

order_label = Label(root,text="What Food Type are you Ordering:",font=20,bg=bg_colour)
order_label.pack(pady=10)

food_type_choice = ["Rice/Pasta","Proteins","Side Dish","Beverage","Soup and Swallows"]
food_type = ttk.Combobox(root,values=food_type_choice)
food_type.pack()

next_button = Button(root,text="Next",command=next_page)
next_button.pack(pady=10)

# Create a close button.
close_button = Button(root, text="Close", command=root.destroy,bg="orangered")
close_button.pack(pady=10)

root.mainloop()