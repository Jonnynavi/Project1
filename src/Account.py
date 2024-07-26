
class Account():
    def __init__(self, username, password, email, role, name, id=None):
        self._id = id
        self._username = username
        self._password = password
        self._email = email
        self._role = role
        self._name = name
        self._cart = []
        self._order_history = []
    



    def get_email(self):
        return self._email
    
    def get_role(self):
        return self._role

    def get_name(self):
        return self._name
    
    def get_username(self):
        return self._username
    
    def get_password(self):
        return self._password
    
    def add_to_cart(self, product):
        self._cart.append(product)
    