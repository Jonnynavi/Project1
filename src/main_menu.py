from Account import Account
from Product import Product
from mysql_logic import *

def login():
    print("please enter your info")
    username = input("Username: ")
    password = input("Password: ")
    account = check_credentials(username, password)
    if account == None:
        print("please try again your email or password was incorrect")
    else:
        return account
    
def create_an_account():
    email = input("Please enter your email")
    while True:
        does_email_exist = find_user_by_email(email)
        if does_email_exist != None:
            print("Email is already in use please try another one")
            email = input("Please enter your email")
            continue
        else:
            break
    username = input("Please create a username")
    while True:
        does_username_exist = find_user_by_username(username)
        if does_username_exist != None:
            print("Username is already in use please try again")
            username = input("Please create a username")
            continue
        else:
            break
        
    password = input("Please create a password")
    first_name = input("Please enter your first name")
    last_name = input("please enter your last name")
    full_name = first_name + " " + last_name
    secret_code = input("if your are a employee please enter the secret code")
    if secret_code == "1234":
        role = "admin"
    else:
        role = "customer"
        
    account = Account(username, password, email, role, full_name)
    insert_user(account)
    print(f"Thank you for creating an account {first_name}")
    return account

def show_products():
    print("Current Items")
    products = get_products()
    for x in products:
        print(x)
        print("#############################")
    return products


def add_to_cart(product:Product, current_user: Account):
    current_user.add_to_cart(product)

# def remove_item_from_cart(current_user: Account):
#     A
 
def check_out(user: Account):
    order = Order(None, user.get_id(),date.today(),user.get_cart())
    insert_into_orders(order)
    print(f"Order #{order.id} has been Placed")
    user.empty_cart()

def get_user_prev_orders(account: Account):
    get_previous_user_orders(account)
    account.get_order_history()

