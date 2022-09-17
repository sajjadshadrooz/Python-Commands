
# values have not repeat.
# set is not indexable.  ( we not have set[0] , ...  )


from ast import comprehension


mySet = { 1 , 1 , 1 , 2 , 2 , 3 , 4 , 4 , 5 } 

print(mySet)  # {1, 2, 3, 4, 5}

mySet = { 't' , 'z' , 1 , 4 , 6 }

############################################################

mySet.add( 'newValue' )  # if newValue exist no change if not exist add to set.

mySet.remove( 'Valuse' ) # if not exist throw error , if exist value deleted.

mySet.discard( 'value' ) # if exsit or not , value delete without error.

copySet = mySet.copy()   # make a copy of mySet.

mySet.clear()            # delete all data of set.

############################################################

oddSet = { 1 , 3 , 5 , 7 , 9 }
evenSet = { 2 , 4 , 6 , 8 , 10 }

print( oddSet | evenSet )   # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print( oddSet & evenSet )   # set()

############################################################

comprehensionSet = { item ** 2 for item in range(10) }