import json


def load_contact():
    try:
        with open("contact.json", "r") as file:
            contacts = json.load(file)
            return contacts

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        print("Error: Contact file contains invalid data.")
        return {}


def save_contact(contact):
    with open("contact.json", "w") as file:
        json.dump(contact, file, indent=4)


def add_contact(contact):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter Email: ")

    contact[name] = {
        "phone": phone,
        "email": email,
    }

    save_contact(contact)

    print("Contact added successfully!")


def view_contacts(contact):
    if not contact:
        print("No contacts found.")
        return

    print("\n======== CONTACTS ========")

    for name, details in contact.items():
        print("Name:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])
        print("----------------")


def search_contact(contact):
    name = input("Enter name to search: ")

    if name in contact:
        print("\nContact found!")
        print("Name:", name)
        print("Phone:", contact[name]["phone"])
        print("Email:", contact[name]["email"])

    else:
        print("Contact not found.")


def update_contact(contact):
    name = input("Enter name to update: ")

    if name not in contact:
        print("Contact not found.")
        return

    print("\nCurrent contact information:")
    print("Phone:", contact[name]["phone"])
    print("Email:", contact[name]["email"])

    phone = input("Enter new phone number: ")
    email = input("Enter new email: ")

    contact[name]["phone"] = phone
    contact[name]["email"] = email

    save_contact(contact)

    print("Contact updated successfully!")


def delete_contact(contact):
    name = input("Enter name to delete: ")

    if name in contact:
        del contact[name]

        save_contact(contact)

        print("Contact deleted successfully!")

    else:
        print("Contact not found.")


def main():

    contact = load_contact()

    while True:

        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contact)

        elif choice == "2":
            view_contacts(contact)

        elif choice == "3":
            search_contact(contact)

        elif choice == "4":
            update_contact(contact)

        elif choice == "5":
            delete_contact(contact)

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice. Please try again.")


main()