import math as m
import time as t
# Finding the root of a cubic equation and a quadratic equation
# Note Python doesn't support square root of a negative number.
def get_quadratic_root(a,b,c):
    try:
        # r = root 
        num = b**2 - 4*a*c
        sqrt = m.sqrt(num)
        r1 = -b + sqrt/2*a
        r2 = -b - sqrt/2*a
        print(f"The roots are: {r1} and {r2}")
    except:
        print("The equation is not quadratic")
def get_cubic_root(a,b,c,d):
    try:
        roots = []
        for i in range(-1000,1000):
            if a * (i**3) + b * (i**2) + c * (i**1) + d == 0:
                roots.append(i)
        for i in roots:
            print(f"The roots are : {i}")
    except:
        print("The equation is not cubic")

def get_quartic_root(a,b,c,d,e):
    try:
        roots = []
        for i in range(-1000,1000):
            if a * (i**4) + b * (i**3) + c * (i**2) + d * (i**1) + e == 0:
                roots.append(i)
        for i in roots:
            print(f"The roots are : {i}")
    except:
        print("The equation is not quartic")
 
print("Welcome to the Root Calculator for a Quadratic , Cubic and Quartic equation!")
t.sleep(1.5)
print("To calculate the root of a quadratic equation, Press 1")
t.sleep(1.5)
print("To calculate the root of a cubic equation, Press 2")
t.sleep(1.5)
print("To calculate the root of a quartic equation, Press 3")
t.sleep(1.5)
choice = int(input("Enter choice >> "))
t.sleep(1)
if choice == 1:
    a = int(input("Enter a >> "))
    b = int(input("Enter b >> "))
    c = int(input("Enter c >> "))
    get_quadratic_root(a,b,c)

elif choice == 2:
    a = int(input("Enter a >> "))
    b = int(input("Enter b >> "))
    c = int(input("Enter c >> "))
    d = int(input("Enter d >> "))
    get_cubic_root(a,b,c,d)

elif choice == 3:
    a = int(input("Enter a >> "))
    b = int(input("Enter b >> "))
    c = int(input("Enter c >> "))
    d = int(input("Enter d >> "))
    e = int(input("Enter e >> "))
    get_quartic_root(a,b,c,d,e)

