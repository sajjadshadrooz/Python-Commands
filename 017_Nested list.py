
nestedList = [  [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 ] , 9 ]

item_1 = nestedList[0]  # [ 1 , 2 , 3 ]
item_2 = nestedList[1]  # [ 4 , 5 , 6 ]
item_3 = nestedList[2]  # [ 7 , 8 ]
item_4 = nestedList[3]  # 9

item_1_sub_item_2 = nestedList[0][1]  # 2

###############################################################

createNestedList = [ [ subItem for subItem in range(1,4) ] for item in range(1,4) ]


