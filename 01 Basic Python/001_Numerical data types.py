
print( type(5) )        # <class 'int'>
print( type(5.3) )      # <class 'float'>
print( type(5j) )       # <class 'complex'>

###############################################

print( 3 + 7 )          # 10
print( 3 + 7.0 )        # 10.0
print( 4.9 - 7 )        # -2.0999999999999996

###############################################

print( 7 * 4 )          # 28
print( 49 / 7 )         # 7.0   Always is float

###############################################

print( 1 + 3 * 8 / 2  )    # 13.0
print( (1 + 3) * 8 / 2  )  # 16.0

###############################################

negativeNumber = -5
madePositive = abs( negativeNumber ) # +5 , 5

###############################################

# variable = sum( iterables )  -> return total of numbers.  Important: all items should be number.
sumation = sum( ( 1 , 2 , 3 , 4 , 5) )