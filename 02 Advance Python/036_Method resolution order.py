class A:
    
    def printHello(self):
        print("Hello from A.")

class B(A):
    
    def printHello(self):
        print("Hello from B.")

class C(A):
    
    def printHello(self):
        print("Hello from C.")

class D(B , C):
    pass



item = D()
item.printHello()  # Hello from B.    -> because of priority.

###########################################

