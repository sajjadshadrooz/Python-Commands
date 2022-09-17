# class Parent:

#     def __init__(self , parentParam1 , parentParam2 , parentParam3):
#         self.parentVariable1 = parentParam1
#         self.parentVariable2 = parentParam2
#         self.parentVariable3 = parentParam3

# class Child(Parent):
#     pass

# user = Child( 'parentArgs1' , 'parentArgs2' , 'parentArgs3' )

################################################################################

class Parent:

    def __init__(self , parentParam1 , parentParam2 , parentParam3):
        self.parentVariable1 = parentParam1
        self.parentVariable2 = parentParam2
        self.parentVariable3 = parentParam3

class Child(Parent):
    def __init__(self , parentParam1 , parentParam2 , parentParam3 , childParam1):
        self.childParam1 = childParam1

        # Way 1 -> This way use when we have multi parent.
        Parent.__init__(self , parentParam1 , parentParam2 , parentParam3)

        # Way 2 -> On this way, we never use self.
        # super().__init__(parentParam1 , parentParam2 , parentParam3)     

user = Child( 'parentArgs1' , 'parentArgs2' , 'parentArgs3', 'childArgs1' )

