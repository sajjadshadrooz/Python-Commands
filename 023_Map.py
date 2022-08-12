
# Map function is a way to make map object ( like list ) , that can use of that for the first time.

# myMap = map( functionName , *iterables )
# myMap = map( lambdaVariable , *iterables )
# myMap = map( lambda , *iterables )


numbers = [ 1 , 2 , 3 , 4 , 5 , 6 ]

double = map( lambda x : x*2 , numbers )

print( double )         # <map object at 0x00000230C433AE90>
print( list(double) )   # [2, 4, 6, 8, 10, 12]
print(list(double))     # []                              # Impotant!!! Map is one-time use.