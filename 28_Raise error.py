
#  raise IndexError('Throw index error')
#  raise ValueError('Throw value error')
#  raise SyntaxError('Throw syntax error')
#  raise TypeError('Throw type error')
#  ...

###################################################

# Example

def colorize( text , color ):
    listOfColors = ( "blue" , "red" , "green" )
    if type(text) is not str:
        raise TypeError(f'{text} must be string!')
    elif color not in listOfColors:
        raise ValueError(f'{color} is not in colors!')
    else:
        pass    #Commands


colorize( "text" , "green" )
    