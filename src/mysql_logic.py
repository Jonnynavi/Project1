from datetime import date
import mysql.connector
import json
from Order import Order
from Account import Account    
from Product import Product           

cnx = mysql.connector.connect(user="root", password="200188348Jt!",
                              host="127.0.0.1", database = "naviecommerce")
cursor = cnx.cursor()

def insert_user(user: Account):
    new_user = f"INSERT INTO user(email, role, name) VALUES('{user.get_email()}', '{user.get_role()}', '{user.get_name()}');"
    cursor.execute(new_user)
    cnx.commit()
    insert_credentials(user)  
  
def insert_credentials(user: Account):
    # print(user.get_id())
    id_sql= f"SELECT id FROM user WHERE email = '{user.get_email()}'; "
    cursor.execute(id_sql)
    id = cursor.fetchone()[0]
    user.set_id(id)

    new_credentials = f"INSERT INTO credentials(userID, username, password) VALUES({user.get_id()}, '{user.get_username()}', '{user.get_password()}');"
    cursor.execute(new_credentials)
    cnx.commit()

def get_products():
    sql = "SELECT * FROM products"
    cursor.execute(sql)
    products = []
    for x in cursor.fetchall():
        product = Product(x[0],x[1],x[2],x[3],x[4])
        products.append(product)
    return products
        
def find_user_by_email(email):
    sql_user = f"SELECT * FROM user WHERE email = '{email}' "
    cursor.execute(sql_user)
    return cursor.fetchone()

def find_user_by_username(username):
    sql_user = f"SELECT * FROM user JOIN credentials ON user.id = credentials.userID WHERE userName = '{username}' "
    cursor.execute(sql_user)
    return cursor.fetchone()

def check_credentials(username, password):
    sql_account = f"SELECT * FROM user JOIN credentials c ON user.id = c.userID WHERE username = '{username}' AND password = '{str(password)}'"
    cursor.execute(sql_account)
    results = cursor.fetchone()
    account = Account(username, password,results[1],results[2],results[3], results[0])
    return account


def insert_into_orders(order: Order):
    sql = "INSERT INTO orders(user_id, ordered_date) VALUES(%s,%s)"
    cursor.execute(sql, (order.user_id, date.today()) )
    order.id = cursor.lastrowid
    insert_into_order_lines(order)
    cnx.commit()

def insert_into_order_lines(order:Order):
    
    sql = """INSERT INTO order_lines(order_id, product_id, price, quantity)
            VALUES(%s, %s, %s, %s)"""
    qry = []
    for x in set(order.products):
        id = x.id
        qry.append((order.id, id, order.get_prices()[id], order.prod_qty()[id] ))
    cursor.executemany(sql, qry)

def get_previous_user_orders(account: Account):
    sql = """SELECT o.id, o.user_id, o.ordered_date, p.title, p.image, p.description,
    ol.price, ol.quantity, p.id FROM orders o JOIN order_lines ol ON o.user_id = %s
    JOIN products p ON ol.product_id = p.id
    WHERE ol.order_id = %s"""

    sql_orders = "SELECT * FROM orders WHERE user_id = %s"
    cursor.execute(sql_orders, [account.get_id()])
    orders_qry = cursor.fetchall()
    order_history = []
    for o in orders_qry:
        products = []
        cursor.execute(sql, (account.get_id(), o[0]) )
        for x in cursor:
            for e in range(x[7]):
                products.append(Product(x[8],x[3],x[4],x[5],x[6]))
        order_history.append(Order(o[0], o[1], o[2], products))
    print(order_history)
    
    
    # print(products)
# # print(finduser_by_username(test_account))

# insert_user(test_account)
# print(test_account.get_id())

# products = [Product(1, "one", None, None, 20.99),Product(1, "one", None, None, 20.99),Product(1, "one", None, None, 20.99), Product(2, "two", None, None, 25.99),  Product(2, "two", None, None, 25.99),  Product(2, "two", None, None, 25.99),  Product(3, "three", None, None, 30.99), Product(3, "three", None, None, 30.99),Product(3, "three", None, None, 30.99),Product(3, "three", None, None, 30.99),Product(3, "three", None, None, 30.99)]
account = Account(None, None, 'e', 'e', 'e', 5)
get_previous_user_orders(account)
# account.set_cart(products)
# account.remove_from_cart(5, 5)
# order = Order(0, 1, 10-14,products)
# insert_into_orders(order)
# print(order.prod_qty())
# order.get_prices()







