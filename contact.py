import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from a file (persistent storage)
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to a file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    if name in contacts:
        print(f"Contact {name} already exists!")
        return
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# Edit an existing contact
def edit_contact(contacts):
    name = input("Enter the contact name to edit: ")
    if name not in contacts:
        print(f"Contact {name} does not exist.")
        return
    phone = input(f"Enter new phone number for {name} (leave blank to keep current): ")
    email = input(f"Enter new email address for {name} (leave blank to keep current): ")
    
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email

    save_contacts(contacts)
    print(f"Contact {name} updated successfully.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} does not exist.")

# Display the menu and handle user input
def menu():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add New Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting the contact management system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
