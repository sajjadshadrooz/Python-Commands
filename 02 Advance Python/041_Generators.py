
# Generator: Create advance iterators.

############################################################

# Way 1: Using yield in functions.

def genCounter(stop):
    current = 0
    while current < stop:
        yield current
        current += 1



print(genCounter(10))          # <generator object genCounter at MemoryID>

generator = genCounter(10)

print(next(generator))        # 0
print(next(generator))        # 1
print(next(generator))        # 2
print(next(generator))        # 3
print(next(generator))        # 4

############################################################

# Way 2: Use Expression.
# That its structure is very similar to list comprehension.

# List Comprehension:
listComprehension = [ item for item in range(10) ] 

# Generator Expression
generator = ( item for item in range(10)  )

############################################################

# Best usage of Generators: When we should create many data that use a lot of memory, instead of lists we use generators.

print( sum( [ item for item in range(1000000) ] ) )   # Very fast but use a lot of momory and sometime raise memory limit error in huge numbers.

print( sum( item for item in range(1000000) ) )       # Slower but use less memory.
