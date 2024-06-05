"""
    Develop a program that allows users to store and manage contact information. 
    The program should provide options to add a new contact by entering their name, 
    phone number, and email address. It should also allow users to view their contact list, 
    edit existing contacts, and delete contacts if needed. The program should store the 
    contacts in memory or in a file for persistent storage.
"""

def add_contact(contacts):
    """Add a new contact to the book."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    contacts[name] = {
        'phone': phone,
        'email': email
    }
    print(f"Contact '{name}' added successfully!")


def view_contact_list(contacts):
    """Display all saved contacts."""
    if not contacts:
        print("No contacts found.")
        return
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")


def update_contact(contacts):
    """Update contact details."""
    name = input("Enter contact name to update: ")
    if name in contacts:
        name_update = input("Enter contact name for update: ")
        phone = input("Enter new phone number (leave blank to skip): ")
        email = input("Enter new email address (leave blank to skip): ")
        
        if name_update:
            contacts[name_update] = contacts.pop(name)
            name = name_update
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")


def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")


def main():
    contacts = {}

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contact_list(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting Contact Book. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()