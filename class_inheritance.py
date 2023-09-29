
# creating parent class 'Members'
class Members:
    # initializes the attributes of the class
    def __init__(self):
        self.name = 'No Name Provided'
        self.phone = 'xxx-xxx-xxxx'
        self.address = ''
        self.member_id= 0 

# creating child class 'Staff' which inherits its parent 'Members' attributes
class Staff(Members):
    # initializes the attributes of the class 
    def __init__(self):
        # this ensures attributes defined in the 'Members' class are
        # properly initialized for instances of child class
        super().__init__()
        self.position: 'services'
        self.employee_discount = '20%'

# creating child class 'Customer' which inher its tits partent 'Members' attributes
class Customer(Members):
    def __init__(self):
        super().__init__()
        self.membership_plan = 'Plan'
        self.mo_payments = 'pay Plan'
