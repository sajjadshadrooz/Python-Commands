
# 1: Create New Version of for loop.

def newFor(iterables , func):

    iterator = iter(iterables)

    while True:
        try:
            temp = next(iterator)
        except:
            break
        else:
            func(temp)

numbers = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
newFor( numbers , print )
newFor(numbers , lambda num: print(num**2))

##########################################################

# 2: Create custom range.

class NewRange:

    def __init__(self , start , stop , step= 1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            num = self.current
            self.current += self.step
            return num
        raise StopIteration

myRange = NewRange(1, 20, 2)

for num in myRange:
    print(num)

##########################################################

# 3: Move in objects.

class User:
    activeUsers = []

    def __init__(self, name , family, age):
        self.name = name
        self.family = family 
        self.age = age
        User.activeUsers.append(dict(name= name , family= family , age= age))

    def __iter__(self):
        self.index = 0       
        return self

    def __next__(self):
        if self.index < len(User.activeUsers):
            person = User.activeUsers[self.index]
            self.index += 1
            return person
        raise StopIteration

sajjad = User("Sajjad" ,"Shadrooz", 23)
erfan = User("Erfan", "Hashemi" , 22)
nima = User("Nima", "Moradi", 25)

for person in sajjad:
    print(person)



