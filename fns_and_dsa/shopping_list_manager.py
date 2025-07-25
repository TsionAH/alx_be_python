shopping_list = []

def add_items():
    while True:
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        more = input("Do you want to add more items? (yes/no): ").lower()
        if more != 'yes':
            break

def remove_items():
    while True:
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")
        more = input("Do you want to remove more items? (yes/no): ").lower()
        if more != 'yes':
            break

def display_items():
    if not shopping_list:
        print("Shopping list is empty.")
    else:
        print("Current Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_items()
        elif choice == '2':
            remove_items()
        elif choice == '3':
            display_items()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
