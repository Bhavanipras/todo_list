import json
import os

FILENAME = 'contacts.json'

def load_contacts():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, 'r') as file:
        return json.load(file)

def save_contacts(contacts):
    with open(FILENAME, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    print("Contact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")

def search_contact(contacts):
    search_term = input("Enter the name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if search_term.lower() in name.lower() or search_term in info['phone']:
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print()
            found = True
    if not found:
        print("No contact found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print("Contact not found.")
        return
    
    print("Leave fields empty to keep existing values.")
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
    email = input(f"Enter new email (current: {contacts[name]['email']}): ")
    address = input(f"Enter new address (current: {contacts[name]['address']}): ")
    
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address

    print(f"Contact '{name}' updated.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

def display_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contacts = load_contacts()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Exiting.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
