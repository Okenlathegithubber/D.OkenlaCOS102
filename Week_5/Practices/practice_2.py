# This value is passed by reference.
# Meaning that as the value inside the function changes, the value outside will change.
def changeme( mylist ):
    #This changes a passed list
    mylist[0] = 100
    mylist.append([1,2,3,4])
    print("Values inside the function: ", mylist)
    return
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

# Result from above
# Values inside the function:  [100, 20, 30, [1, 2, 3, 4]]
# Values outside the function:  [100, 20, 30, [1, 2, 3, 4]]