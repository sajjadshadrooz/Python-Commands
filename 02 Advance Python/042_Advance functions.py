
# Note 1 - We can pass functions to another function.
# Example 1:

def sum(number, func):
    total = 0
    for num in range(1, number + 1):  
        total += func(num)
    return total              # [1,2,3,4,5]

def square(x):
    return x ** 2

print(sum(5, square))

# Example 2:

def sum2(number, func):
    total = 0
    for num in range(1, number + 1):  
        total += func(num)
    return total              # [1,2,3,4,5]


print(sum2(5, lambda item : item ** 2))

##########################################################

# Note 2 - We can create nested functions.
# Example 1:

def greet(person):
    def sayHello():
        msg = 'I\'m glad to meet you '
        return msg

    result = sayHello() + person
    return result

print(greet("Sajjad"))


# Example 2:

def greet2(person):
    def sayHello():
        msg = 'I\'m glad to meet you '
        return msg + person

    return sayHello()         # return the outcome of sayHello function.

print(greet2("Sajjad"))

###########################################################

# Note 3 - We can pass inner function to outcome of base function.
# Example 1:

def greet3(person):
    def sayHello():
        msg = 'I\'m glad to meet you '
        return msg + person

    return sayHello          # return the sayHello function.

func = greet3("Sajjad")

print(func())





