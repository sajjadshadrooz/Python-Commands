
# max()     -> Returns the item with the highest value, or the item with the highest value in an iterable.
# min()     -> Returns the item with the lowest value, or the item with the lowest value in an iterable.
# len()     -> Returns the number of items in an object.

# Examples:

numbers = [3, 6, 8, 13, 4, 90]
chars = ['a', 't', 'z']
myName = "Sajjad"
names = ['Sajjad', 'Milad', 'Akbar', 'Sara', 'Iman','Ali']

print(max(numbers))                               # 90
print(min(numbers))                               # 3

print(max(names, key=lambda name: len(name)))     # Sajjad
print(min(names, key=lambda name: len(name)))     # Ali

print(len(numbers))                               # 6

lenNames = [len(name) for name in names]
print(lenNames)                                   # [6, 5, 5, 4, 4, 3]


#############################################################################

# sorted()     -> Returns a sorted list of the specified iterable object.
# sort()       -> Is a method that sorts the list ascending by default.

# Examples:

numbers = [1, 5, 8, 4, 6, 2]

users = [
            {'name': 'Sajjad', 'family': 'Shadrooz', 'age': 23},
            {'name': 'Sina', 'family': 'Hashemi', 'age': 40},
            {'name': 'Mohammad', 'family': 'Abbasi', 'age': 30},
            {'name': 'Reza', 'family': 'Rahmani', 'age': 80}
        ]


numbers.sort()
print(numbers)                                   # [1, 2, 4, 5, 6, 8]

print(sorted(numbers))                           # [1, 2, 4, 5, 6, 8]

print(sorted(users, key=lambda user: user['age'], reverse=True))


#############################################################################

# reversed()     -> Returns a reversed iterator object.
# reverse()      -> Is a method that reverses the sorting order of the elements.

# Examples:

numbers = [1, 2, 3, 4, 5, 6]

numbers.reverse()
print(numbers)                                   # [6, 5, 4, 3, 2, 1]

print(list(reversed(numbers)))                   # [1, 2, 3, 4, 5, 6]

print(list(reversed("hello")))                   # ['o', 'l', 'l', 'e', 'h']

print(sorted(numbers, reverse=True))             # [6, 5, 4, 3, 2, 1]            Note: It's little slower.

print("hello"[::-1])                             # olleh   

nameRes = ''

print(nameRes.join(list(reversed("hello"))))     # olleh


for num in reversed(range(0, 10)):
    print(num , end='  ')                       # 9  8  7  6  5  4  3  2  1  0