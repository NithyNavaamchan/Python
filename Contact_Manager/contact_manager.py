contacts = [{
    "name": "Alice Smith",
    "phone": "555-1234",
},
{
    "name": "Bob Johnson",
    "phone": "555-5678",
}]

def list_contacts():
    return contacts

def add_contact(name, phone):
    contacts.append({
        "name": name,
        "phone": phone,
    })

def view_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None

def search_contacts(query):
    results = []
    for contact in contacts:
        if query.lower() in contact["name"].lower() or query in contact["phone"]:
            results.append(contact)
    return results

while True:
    print("\n1. Add Contact")
    print("2. View Contact")
    print("3. List Contacts")
    print("4. Search Contacts")
    print("5. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
        print("Contact added.")
    elif choice == "2":
        name = input("Enter name to view: ")
        contact = view_contact(name)
        if contact:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
        else:
            print("Contact not found.")
    elif choice == "3":
        all_contacts = list_contacts()
        for contact in all_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    elif choice == "4":
        query = input("Enter search query: ")
        results = search_contacts(query)
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    elif choice == "5":
        break
    else:
        print("Invalid option. Please try again.")