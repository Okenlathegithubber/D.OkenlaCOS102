# Scope of Variables
# There are two typs of variables:
# 1. Global variables - Variables outside a function
# 2. Local variables - Variables inside a function

total = 50 # This is global variable.
def sum( arg1, arg2 ):
    # Add both the parameters
    total = arg1 + arg2
    print ("Inside the function local total : ", total)
    return total
# Now you can call sum function
sum( 10, 20 )
print ("Outside the function global total : ", total)