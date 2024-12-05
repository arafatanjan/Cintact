
from contact import add_contact, view_contacts, remove_contact, search_contacts
from file_operations import save_contacts_to_file, load_contacts_from_file

def display_menu():
    
    print("\n===== Contact Book Management =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contacts")
    print("5. Load Contacts from File")
    print("6. Exit")


# contacts = load_contacts_from_file()
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")
        add_contact(name, email, phone, address)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        phone = input("Enter the phone number of the contact to remove: ")
        remove_contact(phone)
    elif choice == "4":
        query = input("Enter name or phone to search: ")
        search_contacts(query)
    elif choice == "5":
        load_contacts_from_file()
    elif choice == "6":
        # save_contacts_to_file(contacts)  
        print("Thank you for using the Contact Book Management System!")
        break
    else:
        print("Invalid choice. Please try again.")


