from main_menu import *
from mysql_logic import *

def main():
    
    # while True:
    #     print("Please Login")
    products = get_products()
    print("our current products please select by the num\n")
    num = 0
    for product in products:
        num+=1
        print(f"[{num}]\n {product}")
        print("#################")
    

main()
