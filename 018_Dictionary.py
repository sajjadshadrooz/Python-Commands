
from ast import comprehension


myDictionary = { "key1": "value1" , "key2": "value2" , "key3": "value3" }
myDictionary = dict( key1 = "value1" , key2 = "value2" , key3 = "value3")

###############################################################

valueOfKey = myDictionary["key1"]
valueOfKey = myDictionary.get("key1")  # Recommended! When key not found never return error and return None.

###############################################################

keysOfDict = myDictionary.keys()
valuesOfDict = myDictionary.values()
itemsOfDict = myDictionary.items()  #  [( 'key1' , 'value1' ) , ( 'key2' , 'value2') , ... ]  <class 'tuple'>

###############################################################

isExist = "key2" in keysOfDict      # True , False

###############################################################

myDictionary.clear()   # delete all keys and values.

###############################################################

copyOfDict = myDictionary.copy()

###############################################################

# Generate Default Value.
# { ... }.fromkeys( [ keys like item's list ] , default value )

generate = {}.fromkeys([ "name" ,"family" , "age" ] , None )

################################################################

myDictionary.pop("key1")     # delete key1 and it's value.
myDictionary.popitem()       # delete last item of dict.

################################################################

secondDict = {}
secondDict.update(myDictionary)

myDictionary["newKey"] = "newValue"
myDictionary["oldKey"] = "newValue"

################################################################

comprehensionDict = { key:value for key , value in myDictionary.items()  } 
