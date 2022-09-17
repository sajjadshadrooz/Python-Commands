

#  def functionName ( parameters ):       parameters, defualt params , Args , *args , **kwArgs are optional.
#       Commands
#       return results                    returning results is optional.

#  functionName( arguments )              arguments depend on parameters of functions.

###################################################

# Function without parameters and return.

def myFunction():
    print("This is a test.")

myFunction()

###################################################

# Function with parameters but without return.

def printSum(number1 , number2):
    print( number1 + number2 )

printSum( 2 , 3 )

###################################################

# Function with parameters and return.

def returnSum(number1 , number2):
    return number1 + number2

print( returnSum( 2 , 3 ) )

###################################################

# Defualt params.

def exponent( number , power = 2 ):
    return number ** power

print( exponent(3) )        # This function with one arguments , power get defualt value.
print( exponent( 3 , 4 ) )

###################################################

# functions without argument's order.

def division( divided , divisor ):
    return divided / divisor

print( division( 10 , 3 ) )
# or 
print(  division( divisor = 3 , divided = 10 ) )

###################################################

# Functions with *args  ( def functionName( *args ) )  => get values in tuple mode.

def sumAllNumbers( *numbers ):
    total = 0
    for number in numbers:
        total +=number
    return total

print( sumAllNumbers( 1 , 2 , 3 , 4 , 5 ) )

###################################################

# Functions with **kwargs  ( def functionName( **kwargs ) )  => get key , value in dict mode.

def identityInformation( **informations ):
    for key in informations.keys():
        print( f'- {key}: {informations[key]}.' )

identityInformation(name="Sajjad" , lastname="Shadrooz" , age=23)

###################################################

# The priority of using parameters.

# 1. parameters
# 2. *args
# 3. defualt params
# 4. **kwargs

def printFunc( param1 , param2 , *args , defaultParam = 7 , **kwargs):
    print(param1 , param2 , args , defaultParam , kwargs)

printFunc( 1 , 2 , 6 , name="Sajjad" , lastname="shadrooz" )

####################################################

# How allow list sent to *args function.

def argFunction( *args ):
    print(args)

myList = [ 1 , 2 , 3 , 4 , 5 ]
argFunction( *myList )

####################################################

# How allow dictionary sent to **kwargs function.

def kwargFunction( **kwargs ):
    print(kwargs)

myDict = { "name": "sajjad" , "lastname": "shadrooz" }
kwargFunction( **myDict )



