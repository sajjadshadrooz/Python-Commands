
myList1 = [ 5 , 4, 2, 6 , 1 , 3 , 9 , 7 , 8 ]
myList2 = ['item_3', 'item_4', 'item_2', 'item_5', 'item_1' , 'item_4']

myList1.reverse()
myList2.reverse()
print(myList1)
print(myList2)

#########################################################################

myList1 = [ 5 , 4, 2, 6 , 1 , 3 , 9 , 7 , 8 ]
myList2 = ['item_3', 'item_4', 'item_2', 'item_5', 'item_1' , 'item_4']

myList1.sort()
myList2.sort()
print(myList1)
print(myList2)

#########################################################################

myList2 = ['item_3', 'item_4', 'item_2', 'item_5', 'item_1' , 'item_4']

sentence = " - ".join(myList2)
print(sentence)

#########################################################################

#   list slicing => to make copy of main list.
#   copiedList = list[ start index : end index : step ]

myList1 = [ 5 , 4, 2, 6 , 1 , 3 , 9 , 7 , 8 ]
slicedList = myList1[ 0 : 5 : 2 ]
slicedList = myList1[ 0 : ]
slicedList = myList1[ 0 : 5 ]
slicedList = myList1[ : 5 ]
slicedList = myList1[ 0 : : 2 ]
print(slicedList)