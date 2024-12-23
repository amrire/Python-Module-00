#!/usr/bin/python3


class Contact:
    """A class to manage contacts."""
    def __init__(self, nickname, first_name, last_name, phone_number, darkest_secret):
        """Initialize the contact with a name and phone number."""
        self.nickname = nickname.strip()
        self.first_name = first_name.strip() if first_name else "Unknown"
        self.last_name = last_name.strip() if last_name else "Unknown"
        self.phone_number = phone_number.strip()
        self.darkest_secret = darkest_secret.strip()

    @property
    def phone_number(self):
        """Return the phone number."""
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        """Set the phone number."""
        if value.isdigit():
            self._phone_number = value
        else:
            raise ValueError("Phone number must contain only digits.")

    def __str__(self):
        """Return a string representation of the contact."""
        return f"{self.nickname}"

    def __repr__(self):
        """Return a string representation of the contact."""
        return f"{self.first_name} {self.last_name}"



class PhoneBook:
    """A class to manage a phonebook."""

    def __init__(self):
        """Initialize the phonebook with an empty list."""
        self.contacts = []
        self.max_contacts = 8

    def add_contact(self, contact):
        """Add a contact to the phonebook."""
        if len(self.contacts) >= self.max_contacts:
            self.contacts.pop(0) # Remove the oldest contact
        self.contacts.append(contact)

    def get_contacts_summary(self):
        """Return a summary of the contacts in the phonebook."""
        return [
            (index, contact.first_name, contact.last_name)
            for index, contact in enumerate(self.contacts)
        ]

    def get_contact_details(self, index):
        """Return the details of a contact in the phonebook."""
        return self.contacts[index]


def display_phonebook_ui():
    """Display the phonebook user interface."""
    phonebook = PhoneBook()
    while True:
        command = input("Enter command (ADD, SEARCH, EXIT): ").strip().upper()
        if command == "ADD":
            nickname = input("Enter nickname: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            phone_number = input("Enter Phone Number: ")
            darkest_secret = input("Enter Darkest Secrect: ")
            try:
                contact = Contact(nickname, first_name, last_name, phone_number, darkest_secret)
                phonebook.add_contact(contact)
                print("Contact added successfuly.")
            except ValueError as e:
                print(f"Error: {e}")
        elif command == "SEARCH":
            print(f"{"Index":<10}|{"Nickname":<10}|{"First Name":<10}|{"Last Name":<10}")
            print("-" * 40)
            contacts = phonebook.get_contacts_summary()
            for contact in contacts:
                print(f"{contact[0]:<10}|{contact[1]:<10}|{contact[2]:<10}")
            try:
                index = int(input("Enter index to view details: "))
                contact = phonebook.get_contact_details(index)
                print(f"First Name: {contact.first_name}")
                print(f"Last Name: {contact.last_name}")
                print(f"Nickname: {contact.nickname}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Darkest Secret: {contact.darkest_secret}")
            except ValueError:
                print("Please enter a valid number.")
            except IndexError:
                print("Invalid index. Please try again.")
        elif command == "EXIT":
            print("Exiting phonebook. Goodbye!")
            break
        else:
            print("Invalid command. Please enter ADD, SEARCH, or EXIT.")


if __name__ == "__main__":
    display_phonebook_ui()
