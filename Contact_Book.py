import json
import os

# File to store contact data
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    print("-----------------------------------------")
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    print("-----------------------------------------")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")

def display_contacts(contacts):
    print("-----------------------------------------")
    if not contacts:
        print("No contacts found.")
    else:
        print("\nSaved Contacts:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contacts(contacts):
    print("-----------------------------------------")
    query = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts if query.lower() in contact["name"].lower() or query in contact["phone"]]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")
    else:
        print("No contacts found matching the query.")

def update_contact(contacts):
    print("-----------------------------------------")
    query = input("Enter name or phone number of the contact to update: ")
    for contact in contacts:
        if query.lower() in contact["name"].lower() or query in contact["phone"]:
            print("Current details:")
            print(contact)
            contact["name"] = input("Enter new name (or press Enter to keep current): ") or contact["name"]
            contact["phone"] = input("Enter new phone number (or press Enter to keep current): ") or contact["phone"]
            contact["email"] = input("Enter new email (or press Enter to keep current): ") or contact["email"]
            contact["address"] = input("Enter new address (or press Enter to keep current): ") or contact["address"]
            print("Contact updated successfully!")
            return
    print("No contact found with the given details.")

def delete_contact(contacts):
    print("-----------------------------------------")
    query = input("Enter name or phone number of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if query.lower() in contact["name"].lower() or query in contact["phone"]:
            print("Contact found:")
            print(contact)
            confirm = input("Are you sure you want to delete this contact? (yes/no): ").lower()
            if confirm == "yes":
                contacts.pop(i)
                print("Contact deleted successfully!")
                return
    print("No contact found with the given details.")

def main():
    
    contacts = load_contacts()
    while True:
        print("-----------------------------------------")
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            display_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        

if __name__ == "__main__":
    main()
