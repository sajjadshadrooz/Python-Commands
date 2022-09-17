
# zip()    -> Returns a zip object, which is an iterator of tuples 
#             where the first item in each passed iterator is paired together,
#             and then the second item in each passed iterator are paired together etc.

# Example 1:

numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [5, 6, 7, 8, 9, 10]

result = zip(numbers_1, numbers_2)
print(list(result))                         # [(1, 5), (2, 6), (3, 7), (4, 8), (5, 9)]

result = zip(numbers_1, numbers_2)
print(dict(result))                         # {1: 5, 2: 6, 3: 7, 4: 8, 5: 9}

myList = [(1, 5), (3, 7), (6, 4), (7, 9)]
print(list(zip(*myList)))                   # [(1, 3, 6, 7), (5, 7, 4, 9)]


#########################################################################################

# Example 2:

students = ["Sajjad", "Erfan", "Mohammad"]
midterm = [78, 80, 94]
final = [90, 88, 92]

finalGrades = [pair for pair in zip(students,midterm, final)]


finalGrades = {t[0]: max(t[1], t[2]) for t in zip(students, midterm, final)}


average = zip( students, map(lambda pair: (pair[0] + pair[1]) / 2,zip(midterm, final)))
print(dict(average))



