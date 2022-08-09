
myList = [ "item_1" , "item_2" , "item_3" ]

myList.append("item4")   # append just insert one item 
myList.append(["item_5" ,"item_6"])  # append just insert one item : ['item_1', 'item_2', 'item_3', 'item4', ['item_5', 'item_6']]
print(myList)

#########################################################

myList = [ "item_1" , "item_2" , "item_3" ]

myList.extend(["item4"])     # without [] every characters becomes an item.
myList.extend(["item_5" ,"item_6"])  # ['item_1', 'item_2', 'item_3', 'item4','item_5', 'item_6']
print(myList)

#########################################################

myList = [ "item_1" , "item_2" , "item_3" ]

myList.insert( 1 , "item_4" )     # list.insert( index , item )
myList.insert( -1 , "item_5" )    # this has very important issue. ['item_1', 'item_4', 'item_2', 'item_5', 'item_3']
print(myList)

##########################################################

myList = [ "item_1" , "item_2" , "item_3" ]

myList.clear()  # empty list and delete all items.
print(myList)

##########################################################

myList = [ "item_1" , "item_2" , "item_3" ]

deletedItem = myList.pop() # delete the last item.
print(myList)

##########################################################

myList = [ "item_1" , "item_2" , "item_3" ]

deletedItem = myList.pop(1) # delete the item with index i.
print(myList)

##########################################################

myList = [ "item_1" , "item_2" , "item_3" , "item_2" ]
myList.remove("item_2")     # delete the ''''''first'''''' item with value x.
print(myList)

