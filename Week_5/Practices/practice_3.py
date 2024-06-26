# This value is passed by value.
# Meaning that the value inside the function can change but the value outside will not change.
def changeme( mylist ):
    #This changes a passed List
    mylist = [1,2,3,4]
    print("Values inside the function: ", mylist)
    return
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

# Result from above.
# Values inside the function:  [1, 2, 3, 4]
# Values outside the function:  [10, 20, 30]