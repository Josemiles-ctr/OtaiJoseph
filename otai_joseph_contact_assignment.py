contacts={}
def validate_phone(tel):
    allowed_characters = set("()-0123456789 ")
    if len(tel) not in (10, 12, 14):
        return "Invalid phone number length. Allowed lengths are: 10, 12, 14"
    for char in tel:
        if char not in allowed_characters:
            return f"Invalid character '{char}' in phone number. Allowed characters are digits, parentheses, dash, and space."
    if len(tel) == 14:
        if tel[0] != '(' or tel[4] != ')' or tel[5] != ' ' or tel[9] != '-':
            return "Invalid phone number format. Expected format: (XXX) XXX-XXXX"
    elif len(tel) == 12:
        if tel[3] != '-' or tel[7] != '-':
            return "Invalid phone number format. Expected format: XXX-XXX-XXXX"
    elif len(tel) == 10:
        if not tel.isdigit():
            return "Invalid phone number format. Expected only digits for 10 digit format"
        if tel[0] != "0":
            return "Invalid phone number format. Expected a 0 at the start"
    return None


def validate_email(email):
    if "@" not in email:
        return "Invalid email format. Expected format: XXXX@XXX.XXX"
    local, _, domain = email.partition("@")
    if not local or "." not in domain:
        return "Invalid email format. Expected format: XXXX@XXX.XXX"
    return None


def receive_contact_input():
    user_name = None
    real_name = None
    email = None
    phone = None
    while not user_name:
        user_name = input("Enter username: ")
        if not user_name:
            print("Username cannot be empty. Please try again.")
        elif user_name in contacts:
            print("Username already exists. Please try again.")
            user_name = None
    while not real_name:
        real_name = input("Enter real name: ")
        if not real_name:
            print("Real name cannot be empty. Please try again.")
    while not email:
        email = input("Enter email: ")
        if not email:
            print("Email cannot be empty. Please try again.")
        else:
            error = validate_email(email)
            if error:
                print(error)
                email = None
    while not phone:
        phone = input("Enter phone number: ")
        if not phone:
            print("Phone number cannot be empty. Please try again.")
        else:
            error = validate_phone(phone)
            if error:
                print(error)
                phone = None
    return {user_name: {"user_name": user_name, "real_name": real_name, "email": email, "phone": phone}}

def add_contact():
    contact = receive_contact_input()
    contacts.update(contact)
    print("Contact added successfully.")
    
def view_contact():
    user_name = input("Enter username to view: ")
    if user_name in contacts:
        contact = contacts[user_name]
        print()
        print(f"Username: {contact['user_name']}")
        print(f"Real Name: {contact['real_name']}")
        print(f"Email: {contact['email']}")
        print(f"Phone: {contact['phone']}")
        print()
    else:
        print("Contact not found.")

def update_contact():
    user_name = input("Enter username to update: ")
    if user_name in contacts:
        contact = contacts[user_name]
        print("Leave field empty to keep current value.")
        new_real_name = input(f"Enter new real name (current: {contact['real_name']}): ") or contact['real_name']
        new_email = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
        new_phone = input(f"Enter new phone number (current: {contact['phone']}): ") or contact['phone']
        
        # Validate email and phone
        email_error = validate_email(new_email)
        phone_error = validate_phone(new_phone)
        
        if email_error:
            print(email_error)
            return
        if phone_error:
            print(phone_error)
            return
        
        contacts[user_name] = {"user_name": user_name, "real_name": new_real_name, "email": new_email, "phone": new_phone}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    user_name = input("Enter username to delete: ")
    if user_name in contacts:
        del contacts[user_name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact():
    search_term = input("Enter search term (username, real name, email, or phone): ")
    found_contacts = []
    for contact in contacts.values():
        if (search_term.lower() in contact['user_name'].lower() or
            search_term.lower() in contact['real_name'].lower() or
            search_term.lower() in contact['email'].lower() or
            search_term.lower() in contact['phone']):
            found_contacts.append(contact)
    if found_contacts:
        print("Found contacts:")
        for contact in found_contacts:
            print(f"Username: {contact['user_name']}, Real Name: {contact['real_name']}, Email: {contact['email']}, Phone: {contact['phone']}")
    else:
        print("No contacts found.")

def list_contacts():
    if contacts:
        print("All contacts:")
        for contact in contacts.values():
            print(f"Username: {contact['user_name']}, Real Name: {contact['real_name']}, Email: {contact['email']}, Phone: {contact['phone']}")
    else:
        print("No contacts available.")
    

        
def contact_manager():
    print("=== Contact Manager Menu ===CRUD")
    print("Choose an option to continue:")
    print("1. Add contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. List all contacts")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        search_contact()
    elif choice == '6':
        list_contacts()
    elif choice == '7':
        print("Exiting Contact Manager. Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")
    contact_manager()  # Loop back to the menu after an action
        
        
# Testing
contact_manager()