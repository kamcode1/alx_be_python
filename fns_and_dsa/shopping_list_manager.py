
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter the item to add: "))

        if choice == 1:
            name = input("please provide the name of the item: ")
            item = {"name": name}
            shopping_list.append(item)
            print("Item added Successfully!")
            # Prompt for and add an item
            pass
        elif choice == 2:
            name = input("input item to be removed: ")
            found = False
            for shopping_item in shopping_list:
                if shopping_item["name"] == name:
                  shopping_list.remove(shopping_item)
                  found = True
            if not found:
                print("item not found.")
            # Prompt for and remove an item
            pass
        elif choice == 3:
            if not shopping_list:
                print("item not found")
            else:
                for shopping_item in shopping_list:
                  print(f"Item_name: {shopping_item['name']}")
            # Display the shopping list
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()