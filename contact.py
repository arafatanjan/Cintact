
from file_operations import save_contacts_to_file

contacts = []

def add_contact(name, email, phone, address) :
    for contact in contacts:
        if not isinstance(name, str):
            print("Invalid name! The name must be a non-empty string.")
            return

        if not phone.isdigit():
            print("Invalid phone number! The phone number must be a valid integer.")
            return
        
        if contact['phone'] == phone:
            print("Error: This phone number already exists!")
            return

    new_contact = {'name': name, 'email': email, 'phone': phone, 'address': address}
    contacts.append(new_contact)
    print(f"Contact added successfully!")

    save_contacts_to_file(contacts)

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return    
    print("\nContact Book:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
    print("\n")

def remove_contact(phone):
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print(f"Contact with phone {phone} removed successfully!")
            return
    print("Error: Contact with this phone number not found.")

def search_contacts(query):
    found = False
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print(f"Found: Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
            found = True
    if not found:
        print(f"No contact found matching {query}.")
