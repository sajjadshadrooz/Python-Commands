
# A function like map but has some difference.

# myFilter = filter( myFunctionName , iterables ) 
# myFilter = filter( lambdaVariable , iterables ) 
# myFilter = filter( lambda , iterables ) 

#######################################################


from ast import comprehension
from asyncio import events


numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
evens = filter( lambda num : num % 2 == 0 , numbers )

print( evens )          # <filter object at 0x000001912C780070>
print( list(evens) )    # [2, 4, 6, 8, 10]
print( list(evens) )    # []

######################################################

# ( map and filter together ) vs ( comprehension )

users = [
    { "name": "Sajjadd" , "lastname": "Shadrooz" , "age": 23  },
    { "name": "Saman" , "lastname": "Karimi" , "age": 18  },
    { "name": "Elham" , "lastname": "Mohammadi" , "age": 15  },
]

mapFilterMoudle = map( lambda user : user["name"] , filter( lambda user : user["age"] > 17 , users ) )
comprehensionMoudle = [ user["name"] for user in users if user["age"] > 17  ]
