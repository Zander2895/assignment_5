shopping_list = []

def add_item(item):
    shopping_list.append(item)

def remove_item(item):
    shopping_list.remove(item)

def print_shopping_list():
    for item in shopping_list:
        print(f"Item: {item}")

while True:
    print("""
    1. Add item
    2. Remove item
    3. Print shopping list
    """)
    user_option = int(input("Input the option that you would like to perform: "))
    if user_option == 1:
        user_item = input("What is the item you would like to add: ")
        add_item(item= user_item)
        print("The item was added to the list! ")
    elif user_option == 2:
        item_to_remove = input("What is the item that you would like to remove: ")
        remove_item(item = item_to_remove)
        print("The item was removed from the list! ")
    elif user_option == 3:
        print_shopping_list()
    else:
        print("Invalid option choosen! ")