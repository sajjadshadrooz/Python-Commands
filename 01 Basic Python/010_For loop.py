
#    for item in collection:
#        Commands for each item.  

#    collection => list of numbers , list of characters in strings , range numbers , etc.
#    item => each item of collection.
#    break => use in commads when want to terminate and close 'for'.

collection = [ 4 , 2 , 3 , 1 , 5]
for item in collection:
    print(item ** item)

collection = 'Sajjad'
for item in collection:
    print(item)

collection = range(1,6)
for item in collection:
    print(item * 2)