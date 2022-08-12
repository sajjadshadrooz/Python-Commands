
# Like an arrow function , anonymous Functions or simple fuction that has not name and written in one line.

#  variable = lambda params : returning commands

myLambda = lambda num : num ** 2
myLambda2 = lambda num , power : num ** power

def myFucntion(num):
    return num ** 2

print( myFucntion(3) )
print( myLambda(3) )

#######################################################

# lambda never has name , however put in one variable.

print( myLambda.__name__ )       # <lambda>
print( myFucntion.__name__ )     # myFucntion