
# class range : List of regular numbers.
# collection = range( strat , stop , step )

# start: the number that list start with.
# stop:  the number that list is less than.
# step:  the number that gap of each number is.

print( range(1,11) )           # range(1, 11)
print( list(range(1,11)) )     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print( range(1,11,2) )         # range(1, 11, 2)
print( list(range(1,11,2)) )   # [1, 3, 5, 7, 9]

print( list(range(10)) )       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print( list(range(10,0,-1)) )  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]