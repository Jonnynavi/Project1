import datetime
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
    print(cursor.fetchone())
    cnx.commit()
    cnx.close()

def get_products():
    sql = f"SELECT * FROM products"
    cursor.execute(sql)
    products = []
    for x in cursor:
        product = Product(x[0],x[1],x[2],x[3],x[4])
        products.append(product)
    return products
        
def create_order(order: Order):
    sql_order = f"INSERT INTO order(user_id, ordered_date) VALUES({order.user_id}, {datetime.today().strftime('%Y-%m-%d')})"
    sql_order_line =f"INSERT INTO order_line()"

def find_user_by_email(email):
    sql_user = f"SELECT * FROM user WHERE email = '{email}' "
    cursor.execute(sql_user)
    return cursor.fetchone()

def find_user_by_username(account: Account):
    sql_user = f"SELECT * FROM user JOIN credentials ON user.id = credentials.userID WHERE userName = '{account.get_username()}' "
    cursor.execute(sql_user)
    return cursor.fetchone()

test_account = Account('jojo', '000', 'jonathan.tor@live.com', 'admin','Jonathan Torres')
# print(find_user_by_username(test_account))

insert_user(test_account)







