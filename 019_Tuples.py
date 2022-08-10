
# tuple's items never change - immutable list
# tuples never update.
# Tuples are very fast. ( Faster than list)


myTuple = ( 1 , 2 , 3 , 4 , 5 )
myTuple = tuple([ 1 , 2 , 3 , 4 , 5 ])  # items should be in list to make tuple.

item_3 = myTuple[2]

#########################################################

locations = {
    (35.67 , 15.21) : "Tehran",
    (45.13 , 12.17) : "Qazvin"
}

locations = {
   "Tehran" : (35.67 , 15.21),
   "Qazvin" : (45.13 , 12.17)
}

##########################################################

myTuple.count(3)

##########################################################

myTuple.index(3) # tuple.index( value , start , stop  )   -   always return just first item that is match.