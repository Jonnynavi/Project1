from main_menu import *

def main():
    while True:
        print("\nWelcome to Navizon!")
        print("#############################")
        current_Account = section_1()

        while True:
            print("Please choose from these options")
            option = int(input("1. shop\n2. check cart\n3. edit cart\n4. checkout\n5. check your past orders\n0. quit\n"))
            print("#############################")

            match option:
                case 1: 
                    shop(current_Account)
                case 2:
                    current_Account.get_price_line()
                case 3:
                    edit_cart(current_Account)
                case 4:
                    check_out(current_Account)
                case 5:
                    get_previous_user_orders(current_Account)
                
                case _:
                    return

def section_1():
    current_account = None
    while True:
        option_1 = input(f"Please Login or create a new account\n1.Login\n2.Create an account\n")
        if option_1 == "1":
            current_account = login()
        elif option_1 == "2":
            current_account = create_an_account()
        
        if current_account == None:
            continue
        
        return current_account

def shop(account:Account):
    products = show_products()
    while True:
        try:
            product_id = int(input("Please enter the the id of the product you want or enter 0 to Quit\n"))
            if product_id == 0:
                break
            qty = int(input("How many would you like?\n"))
        except ValueError:
            print("invalid option, please only enter from the avai lable options")
            continue
        selected_product = [e for e in products if e.id == product_id]
        try:
            account.add_to_cart(selected_product[0], qty)
        except IndexError:
            print("There is currently no product with that id")
            continue
        account.get_price_line()       
        
# test_account = Account('jonaa', '000', 'tooaassd.sdstor@live.com', 'admin','Jonathan Torres')
# shop(test_account)

def edit_cart(account: Account):
    while True:
        account.get_price_line()
        selection = input("Please select from the following\n1.increase quantity of an item\n2.reduce quantity of an item\n0. to quit")

        match selection:
            case "1":
                id = input("Please Enter the item id")
                qty = input("Please Enter how many more you want to add to the qty")
                account.increase_qty_cart(int(id), int(qty))
            case "2":
                id = input("Please Enter the item id")
                qty = input("Please Enter the amount you want to reduce the item by")
                account.reduce_qty_cart(int(id), int(qty))
            case _ :
                break
    account.get_price_line()
main()