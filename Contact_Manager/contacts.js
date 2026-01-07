const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let contacts = [
  { name: "Alice Johnson", phone: "555-1234" },
  { name: "Bob Smith", phone: "555-5678" },
];

function ask(question) {
  return new Promise((resolve) => {
    rl.question(question, resolve);
  });
}

function add_contact(name, phone) {
  for (let contact of contacts) {
    if (contact.name.toLocaleLowerCase() === name.toLocaleLowerCase()) {
      console.log("Contact already exists.");
      return;
    } else {
      contacts.push({ name, phone });
      console.log("Contact added successfully.");
    }
  }
}

function list_contacts() {
  if (contacts.length === 0) {
    console.log("No contacts found.");
    return;
  } else {
    console.log(`\n Total Contacts: ${contacts.length}`);
    for (let contact of contacts) {
      console.log(`Name: ${contact.name}, Phone: ${contact.phone}`);
    }
  }
}

function getContactByName(name) {
  for (let contact of contacts) {
    if (contact.name.toLocaleLowerCase() === name.toLocaleLowerCase()) {
      return contact;
    }
  }
  return null;
}

function searchContact(query) {
  return contacts.filter(
    (c) =>
      c.name.toLocaleLowerCase().includes(query.toLocaleLowerCase()) ||
      c.phone.includes(query)
  );
}

async function main() {
  while (true) {
    console.log("\nContact Manager");
    console.log("1. Add Contact");
    console.log("2. view Contacts");
    console.log("3. list Contacts");
    console.log("4. Search Contact");
    console.log("5. Exit");

    const choice = await ask("Choose an option: ");

    switch (choice) {
      case "1":
        const name = await ask("Enter contact name: ");
        const phone = await ask("Enter contact phone: ");
        add_contact(name, phone);
        break;
      case "2":
        const contactName = await ask("Enter contact name to view: ");
        const contact = getContactByName(contactName);
        if (contact) {
          console.log(`Name: ${contact.name}, Phone: ${contact.phone}`);
        } else {
          console.log("Contact not found.");
        }
        break;
      case "3":
        list_contacts();
        break;
      case "4":
        const query = await ask("Enter name or phone to search: ");
        const results = searchContact(query);
        if (results.length > 0) {
          for (let contact of results) {
            console.log(`Name: ${contact.name}, Phone: ${contact.phone}`);
          }
        } else {
          console.log("No contacts found matching the query.");
        }
        break;
      case "5":
        console.log("Exiting Contact Manager.");
        rl.close();
        return;
      default:
        console.log("Invalid option. Please try again.");
        break;
    }
  }
}

main();
