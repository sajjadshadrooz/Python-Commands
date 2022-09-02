class User:

    def __init__(self , name , family , age):
        self.name = name
        self.family = family
        self._age = age

    ################################################
    # Way 1:

    # Getter method.
    def get_age(self):
        return self._age

    # Setter method.
    def set_age(self , age):
        self._age = age

    ################################################
    # Way 2:

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if value > 0:
            self._age = value
        else:
            raise ValueError('Age value can not be negetive.')

    @property
    def showFullName(self):
        return f'{self.name} {self.family}'

        
##########################################################
# Test way 1:
sajjad = User('Sajjad' , 'Shadrooz' , 23)

print(sajjad.get_age())

sajjad.set_age(24)

##########################################################
# Test way 2:

print(sajjad.age)

sajjad.age = 21

print(sajjad.age)

print(sajjad.showFullName)
