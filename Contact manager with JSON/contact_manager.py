import json
import os

File_NAME = 'data\contacts.json'

def load_contacts():
    if not os.path.exists(File_NAME):
        return []
    try:
        with open(File_NAME, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    
def add_contact(name, phone):
    contacts = load_contacts()
    for c in contacts:
        if c['name'] == name:
            print(f"Contact with name '{name}' already exists.")
            return
    contacts.append({'name': name, 'phone': phone})
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def save_contacts(contacts):
    with open(File_NAME, 'w') as file:
        json.dump(contacts, file, indent=4)

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. Name: {c['name']}, Phone: {c['phone']}")

def search_contact(name):
    contacts = load_contacts()
    for c in contacts:
        if c["name"].lower() == name.lower():
            print(f"Found contact - Name: {c['name']}, Phone: {c['phone']}")
            return
    print(f"No contact found with name '{name}'.")

def delete_contact(name):
    contacts = load_contacts()
    updated_contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    if len(contacts) == len(updated_contacts):
        print(f"No contact found with name '{name}'.")
        return
    save_contacts(updated_contacts) 
    print(f"Contact '{name}' deleted successfully.")

def main():
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == '5':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
