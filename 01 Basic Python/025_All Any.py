
# variable = all( iterables ) : if all item of iterable True , return True else False.
# variable = any( iterables ) : if one item of iterable True , return True else False.

#########################################################################

allVariable = all( 0 , 1 , 2, 3 , 4 , 5 ) # return False , because of 0 item.
allVariable = all( False , True , True , True , True , True ) # return False , because of False.
# ...

#########################################################################

anyVariable = any( 0 , 0 , 0 , 0 , 0 , 0 ) # return False , because all items are 0.
anyVariable = any( False , True , True , True , True , True ) # return True , because we have True item.
# ...