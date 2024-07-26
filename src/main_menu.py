from Account import Account
from Product import Product
from mysql_logic import *

def login():
    print("Please login")
    username = input("Username: ")
    password = input("Password: ")
    #logic will find user on db if not there return no user found please try again
    return Account(0, 'fake@email.com', 'admin','Jonathan Torres')

def create_an_account():
    email = input("Please enter your email")
    while True:
        does_email_exist = find_user_by_email(email)
        if does_email_exist != None:
            print("Email is already in use please try another one")
            continue
        else:
            break
    username = input("Please create a username")
    while True:
        does_username_exist = does_username_exist(username)
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
    if secret_code == 1234:
        role = "admin"
    else:
        role = "customer"
        
    account = Account(username, password, email, role, first_name )

    


def add_to_cart(product:Product, current_user: Account):
    current_user.add_to_cart(product)

# def remove_item_from_cart(current_user: Account):
#     A

def 
