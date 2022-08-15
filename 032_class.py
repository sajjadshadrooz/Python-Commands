
# class ClassName:    < first character of name should be upper case. >
# 
#       <Location of instance attributes>  instance is the self variables
#       nameInstanceVariable1
#       nameInstanceVariable2 
#       ...
# 
#       #################################################################################
#     
#       < Locaion of class attributes >
#       nameVariable1
#       nameVariable2
#       ...
#       
#       ClassName.nameVariable1 = value
#       
#
#       #################################################################################
#
#       < constructor Methods>
#       def __init__( self , ...<parameters1> )  <self name can change like this,me,... >
#           self.parameters = parameters
#           ...
#           ClassName.nameVariable = value
#           ...
#
#       #################################################################################
#
#       < Representation Method >              < Description of class >
#       def __repr__(self):                    <self name can change like this,me,... >
#            return '< class "ClassName" , "Collectiong" >'
#
#       < Representation Method >              < Description of class >
#
#       @classmethod
#       def __repr__(cls):                    <cls name can change like thisClass,... that refer to base class> 
#            return '< class "ClassName" , "Collectiong" >'
#
#

class Users:

    # instance attributes
    name = None
    family = None
    age = None

    # class attributes
    countOfUsers = 0

    def __init__( self , gotName , gotFamily , gotAge ):
        self.name = gotName
        self.family = gotFamily
        self.age = gotAge
        Users.countOfUsers += 1

    def __repr__(self):                 
        return f'<class "{__class__.__name__}" , "Documenting .{self.name}. information">'

    # @classmethod
    # def __repr__(cls):                 
    #     return f'<class "{cls.__name__}">'
    

print(Users.countOfUsers)                       # 0

sajjad = Users("Sajjad" , "Shadrooz" , 23)     

print(sajjad.countOfUsers)                      # 1

print(Users.countOfUsers)                       # 1

ali = Users("Ali" , "Mahmoodi" , 25)

print(ali.name)                                 # Ali

print(sajjad.name)                              # Sajjad

print(sajjad)                                   # <class "Users" , "Documenting .Sajjad. information">

