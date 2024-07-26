class Order():
    def __init__(self, id, user_id, order_date, products=[]):
        self.id = id
        self.user_id = user_id
        self.order_date = order_date
        self.products = products

    def add_product(self, product):
        self.products.append(product)
    
    