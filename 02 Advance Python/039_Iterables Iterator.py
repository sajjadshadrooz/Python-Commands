# iterable  =>  Objects that prepare to iterate
# iterator  =>  Objects that prepared to iterate and cursor index is set.

# Iterables abd iterators use in the loops like for, ... .

numbers = [1, 2, 3, 4, 5, 6]         # Iterable
colors = ('red', 'green', 'blue')    # Iterable
nums = {1, 2, 3, 4, 5, 6}            # Iterable
name = 'Sajjad'                      # Iterable
# ...

# iterable => iter() => iterator

iterNums = iter(nums)               # Iterator

print(iterNums)                     # <set_iterator object at MemoryID>.

print(next(iterNums))               # The cursor of iterate is 0.
print(next(iterNums))               # The cursor of iterate is 1.
print(next(iterNums))               # The cursor of iterate is 2.
print(next(iterNums))               # The cursor of iterate is 3.
print(next(iterNums))               # The cursor of iterate is 4.
print(next(iterNums))               # The cursor of iterate is 5.
print(next(iterNums))               # The cursor of iterate is 6. => raise Out of range error (Stop Iteration) .


iterName = iter(name)
print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))
