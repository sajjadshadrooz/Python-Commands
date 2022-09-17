
item_1 = "value item 1"
item_2 = "value item 2"
item_3 = "value item 3"

myList = [item_1 , item_2 , item_3]
myList = list([item_1 , item_2 , item_3])

#################################################

# len(): The number of items in the list.  <class 'int'>
print( len(myList) )

#################################################

# Indexes
# Ascending IDs: Items ID's start from '0' to 'len(list) - 1'.  < Defualt and primary >
# Descending IDs: Items ID's start from '-1' to 'len(list)*(-1)'.
print( myList[0] )
print( myList[1] )
print( myList[2] )

#################################################

isExistItem3 = "value item 3" in myList      # True,False

