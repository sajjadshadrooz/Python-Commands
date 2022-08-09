
# [expression for member in iterable]

numbers = list(range(10))

comprehension = [ item for item in numbers ]
comprehension = [ item * 2 for item in numbers ]
comprehension = [ item for item in numbers if item %2 == 0 ]  # Even numbers
comprehension = [ item for item in numbers if item %2 != 0 ]  # Odd numbers
comprehension = [ item * 2 if item % 2 == 0 else item * 3 for item in numbers ]