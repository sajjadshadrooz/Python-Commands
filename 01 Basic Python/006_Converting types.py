
# Interpolations - Converting Types

integerVariable = 80                # <class 'int'>
floatVariable = 80.30               # <class 'float'>
stringNumber = "600"                # <class 'str'>

converted = float(integerVariable)  # <class 'float'>
converted = str(integerVariable)    # <class 'str'>
converted = int(floatVariable)      # <class 'int'>
converted = int(stringNumber)       # <class 'int'>

#####################################################

roundUp = int(floatVariable) + 1    # <class 'int'>
roundDown = int(floatVariable)      # <class 'int'>
roundReducer = round(floatVariable , 1)
