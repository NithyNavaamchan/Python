contacts = [
    {"name": "Alice Smith", "phone": "555-1234"},
    {"name": "Bob Johnson", "phone": "555-5678"},
]

def add_contact(name, phone):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact already exists.")
            return
    else:
        contacts.append({"name": name, "phone": phone})
        print("Contact added successfully.")

def list_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print(f"\nTotal contacts: {len(contacts)}")
    for contact in contacts:
        print(f"{contact['name']}-{contact['phone']}")

def get_contact_by_name(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None

def serch_contacts(query):
    return [
        c for c in contacts
        if query.lower() in c["name"].lower() or query in c["phone"]
    ]

while True:
    print("\n1. Add Contact")
    print("2. View Contact")
    print("3. List Contacts")
    print("4. Search Contacts")
    print("5. Exit")

    choice = input("choose an option:")

    if choice == "1":
        add_contact(input("Enter name: "), input("Enter phone number: "))
    elif choice == "2":
        contact = get_contact_by_name(input("Enter name to view: "))
        if contact:
            print(f"{contact['name']}-{contact['phone']}")
        else:
            print("Contact not found.")
    elif choice == "3":
        list_contacts()
    elif choice == "4":
        results = serch_contacts(input("Enter search query: "))
        if results:
            for c in results:
                print(f"{c['name']}-{c['phone']}")
        else:
            print("No matching contacts found.")
    elif choice == "5":
        print("Exiting Contact Manager.")
        break
    else:
        print("Invalid option. Please try again.")
        