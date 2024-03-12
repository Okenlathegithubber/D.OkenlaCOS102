# This python program is used to generate Simple Interest, Compound Interest and Annuity Plan
import time

# The Functions are used to calculate the and Annuity Plan along side the Simple and Compound Interest
def SI(p,r,t):
    a = p * (1 + ( r / 100 ) * t)
    return a

def CI(p,r,n,t):
    power = n * t
    a = p * ( 1 + r / n ) ** power
    return a

def AP(p,r,n,t):
    power = n * t
    a = p * ((( 1 + r / n ) ** power) - 1) / (r / n)
    return a

print("Welcome to the Interest Calculator\n")
time.sleep(1.5)
print("This program is calculating Simple Interest, Compound Interest and Annuity Plan\n")
time.sleep(1.5)
print("To calculate Simple Interest, Enter 1\n")
time.sleep(1.5)
print("To calculate Compund Interest, Enter 2\n")
time.sleep(1.5)
print("To calculate Annuity Plan, Enter 3\n")
time.sleep(1.5)

choice = int(input("What do you wish to Calculate? >> "))

if choice == 1:
    p = int(input("Enter initial principal balance >> "))
    r =  int(input("Enter annual interest rate >> "))
    t = int(input("Enter time (in years) >> "))

    si=SI(p,r,t)
    print(f"Final Amount = N{si}")

elif choice == 2:
    p = int(input("Enter initial principal balance >> "))
    r =  int(input("Enter interest rate >> "))
    n = int(input("Enter number of times interest applied per time period >> "))
    t = int(input("Enter number of time periods elapsed >> "))
    
    ci=CI(p,r,n,t)
    print(f"Final Amount = N{ci}")

elif choice == 3:
    pmt = int(input("Enter the period cash payment >> "))
    r =  int(input("Enter interest rate >> "))
    n = int(input("Enter number of times interest applied per time period >> "))
    t = int(input("Enter number of time periods elapsed >> "))
    
    ap=AP(pmt,r,n,t)
    print(f"Final Amount = N{ap}")