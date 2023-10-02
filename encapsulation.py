

# creating class using encapsulation
class EncapClass:
    def __init__(self):
        self._protected_var = 5 # protected attribute
        self.__private_var = 10 # private attribute


    # get method for protected_var
    def get_protected_var(self):
        return self._protected_var


    # set method for procted_var
    def set_protected_var(self, value):
        self._protected_var = value


    # get method for private_var
    def get_private_var(self):
        return self.__private_var


    # set method for private_var
    def set_private_var(self, value):
        self.__private_var = value
    

# creating an object of EncapClass
def getEncap(obj):
    # accessing private and protected attributes
    print('Protected variable: {}'.format(obj.get_protected_var()))# output: Protected variable: 10
    print('Private variable: {}'.format(obj.get_private_var())) # output: Private variable: 5

def updateEncap(obj):
    # using set moethod to update private and protected attributes
    obj.set_protected_var(35)
    obj.set_private_var(45)
        
    print('Updated protected variable: {}'.format(obj.get_protected_var())) # output: updated protected variable: 35
    print('Updated private variable: {}'.format(obj.get_private_var())) # output: updated private variable: 45




if __name__ == "__main__":
    obj = EncapClass() # creates instance of EncapClass
    getEncap(obj)
    updateEncap(obj)
