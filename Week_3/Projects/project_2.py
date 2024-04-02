# You have been employed as a full-stack developer to write a python program for Izifin Technology, a Fintech company in Nigeria with about 2500 staff strength with
# various years of work experience. Develop a program that takes as input the years of experience and the age of the staff. 
# If the staff has more than 25 years of experience and age is equal to or more than 55, then the Annual Tax Revenue (ATR) of the staff is N5,600,000. If the staff has
# more than 20 years of experience and age is equal to or more than 45, then the ATR should be N4,480,000. If the staff has more than 10 years of experience and age is
# equal to or more than 35, then the ATR should be N1,500,000. Else, for staff less than 10 years of work experience and below 35 years of age, the ATR should be 550,000.

# Create a function named annual_tax_revenue that takes as input the years of experience and the age of the staff.
def annual_tax_revenue(years_of_experience,age):
    if years_of_experience > 25 and age >= 55:
        print("Your annual tax revenue is N5,600,000") 
    elif years_of_experience > 20 and age >= 45:
        print("Your annual tax revenue is N4,480,000")
    elif years_of_experience > 10 and age >= 35:
        print("Your annual tax revenue is N1,500,000")
    else:
        if years_of_experience < 10 and age < 35:
            print("Your annual tax revenue is N550,000")
        else:
            print("Error; Cannot Calculate your annual tax revenue")

try:
    years_of_experience = int(input("Enter years of experience >> "))

    age = int(input("Enter age >> "))

    annual_tax_revenue(years_of_experience,age)
except: 
    print("Invalid Input")