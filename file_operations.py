
import os


def save_contacts_to_file(contacts, file_name="contacts.txt"):
    with open(file_name, 'w') as f:
        for contact in contacts:
            contact_line = f"{contact['name']},{contact['email']},{contact['phone']},{contact['address']}\n"
            f.write(contact_line)
    print("Contacts saved to file.")

def load_contacts_from_file(file_name="contacts.txt"):
    local_contacts = []
    if not os.path.exists(file_name):
        print("No contact file found. Starting fresh.")
        return

    with open(file_name, 'r') as f:
        for line in f:
            name, email, phone, address = line.strip().split(',')
            local_contacts.append({'name': name, 'email': email, 'phone': phone, 'address': address})
    print(f"{local_contacts}")
    return local_contacts