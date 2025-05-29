import os
from datetime import datetime

class Contacts:
    def __init__(self):
        self.contacts = []

    def add(self, name, phone, email, address):
        new_contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address,
            'added_on': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.contacts.append(new_contact)
        print("\nContact saved")

    def show_all(self):
        if len(self.contacts) == 0:
            print("\nNo contacts found")
            return

        self.display_list(self.contacts)

    def find(self, search_text):
        search_text = search_text.lower()
        results = []
        
        for c in self.contacts:
            if search_text in c['name'].lower() or search_text in c['phone']:
                results.append(c)

        if results:
            print("\nFound contacts:")
            self.display_list(results)
        else:
            print("\nNo matching contacts")

    def edit(self, idx, field, value):
        if idx < 0 or idx >= len(self.contacts):
            print("\nInvalid contact number")
            return
            
        if field not in ['name', 'phone', 'email', 'address']:
            print("\nInvalid field")
            return
            
        self.contacts[idx][field] = value
        print(f"\nUpdated {field}")

    def remove(self, idx):
        if idx < 0 or idx >= len(self.contacts):
            print("\nInvalid contact number")
            return
            
        removed = self.contacts.pop(idx)
        print(f"\nRemoved contact: {removed['name']}")

    def display_list(self, contact_list):
        print("\nContacts:")
        for i, c in enumerate(contact_list):
            print(f"{i+1}. {c['name']}")
            print(f"   Phone: {c['phone']}")
            print(f"   Email: {c['email']}")
            print(f"   Address: {c['address']}")
            print("-" * 40)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_phone(phone):
    phone = phone.replace('-', '').replace(' ', '')
    return phone.isdigit() and len(phone) >= 10

def check_email(email):
    return '@' in email and '.' in email and len(email) > 5

def get_input(prompt, validator=None, error_msg=None):
    while True:
        val = input(prompt).strip()
        if not validator or validator(val):
            return val
        print(error_msg or "Invalid input")

def check_number(num):
    try:
        n = int(num)
        return n > 0
    except:
        return False

def main():
    contacts = Contacts()
    
    while True:
        clear()
        print("\nContact Manager")
        print("1. New Contact")
        print("2. Show All")
        print("3. Search")
        print("4. Edit")
        print("5. Delete")
        print("6. Quit")

        choice = input("\nChoice (1-6): ").strip()

        if choice == '1':
            print("\nNew Contact:")
            name = input("Name: ").strip()
            
            phone = get_input(
                "Phone: ",
                check_phone,
                "Enter valid phone number (min 10 digits)"
            )
            
            email = get_input(
                "Email: ",
                check_email,
                "Enter valid email"
            )
            
            address = input("Address: ").strip()
            contacts.add(name, phone, email, address)

        elif choice == '2':
            contacts.show_all()

        elif choice == '3':
            query = input("\nSearch (name/phone): ").strip()
            contacts.find(query)

        elif choice == '4':
            contacts.show_all()
            num = input("\nContact number to edit: ")
            
            if check_number(num):
                idx = int(num) - 1
                print("\nWhat to edit?")
                print("1. Name")
                print("2. Phone")
                print("3. Email") 
                print("4. Address")
                
                field = input("Choice (1-4): ").strip()
                fields = {
                    '1': ('name', None),
                    '2': ('phone', check_phone),
                    '3': ('email', check_email),
                    '4': ('address', None)
                }
                
                if field in fields:
                    field_name, validator = fields[field]
                    new_val = get_input(
                        f"New {field_name}: ",
                        validator,
                        f"Enter valid {field_name}"
                    )
                    contacts.edit(idx, field_name, new_val)
                else:
                    print("\nInvalid choice")
            else:
                print("\nInvalid number")

        elif choice == '5':
            contacts.show_all()
            num = input("\nContact number to delete: ")
            
            if check_number(num):
                idx = int(num) - 1
                contacts.remove(idx)
            else:
                print("\nInvalid number")

        elif choice == '6':
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
# 