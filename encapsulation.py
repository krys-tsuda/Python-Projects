

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
    


def get_attributes(obj):
    # accessing private and protected attributes
    print('Protected variable:', obj.get_protected_var())
    print('Private variable:', obj.get_private_var())

def update_attributes(obj):
    # using set method to update private and protected attributes
    obj.set_protected_var(35)
    obj.set_private_var(45)  
    print('Updated protected variable:', obj.get_protected_var())
    print('Updated private variable:', obj.get_private_var())




if __name__ == "__main__":
    obj = EncapClass() # creates instance of EncapClass
    get_attributes(obj)
    update_attributes(obj)
