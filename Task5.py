import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {'name': self.name, 'phone': self.phone, 'email': self.email}

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [Contact(**contact) for contact in json.load(file)]
        return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)

    def add_contact(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()

    def view_contacts(self):
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def edit_contact(self, index, name=None, phone=None, email=None):
        if 0 <= index < len(self.contacts):
            if name:
                self.contacts[index].name = name
            if phone:
                self.contacts[index].phone = phone
            if email:
                self.contacts[index].email = email
            self.save_contacts()
        else:
            print("Contact not found.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            self.save_contacts()
        else:
            print("Contact not found.")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.view_contacts()
            index = int(input("Enter the contact number to edit: ")) - 1
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email address (leave blank to keep current): ")
            manager.edit_contact(index, name if name else None, phone if phone else None, email if email else None)
        elif choice == '4':
            manager.view_contacts()
            index = int(input("Enter the contact number to delete: ")) - 1
            manager.delete_contact(index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
