
# Logical Operators.  ( and , or , not )

####################################################

userAge = 19
userGender = 'male'

if userAge >= 18 and userGender == 'male':
    print('You have to got to soldiery.')
else:
    print('You can stay at home.')

print(f'True and True is { True and True }.')
print(f'True and False is { True and False }.')
print(f'False and True is { False and True }.')
print(f'False and False is { False and False }.')

####################################################

weather = 'sunny'

if weather == 'sunny' or weather == 'cloudy':
    print("You can travel.")
else:
    print("You can not travel.")

print(f'True or True is { True or True }.')
print(f'True or False is { True or False }.')
print(f'False or True is { False or True }.')
print(f'False or False is { False or False }.')

####################################################

isBrotherComming = False

if not isBrotherComming:
    print("My Brother stay at home.")

print(f'not True is { not True }.')
print(f'not False is { not False }.')

