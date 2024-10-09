import re

def parse_input(user_input):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args

def is_valid_phone(phone):
    
    return (re.match(r'^\+?\d{12}$', phone) or 
            re.match(r'^38\d{10}$', phone) or 
            re.match(r'^\d{10}$', phone))

def validate_contact(name, phone, contacts):
    name = name.lower()

    if not is_valid_phone(phone):
        print("Invalid phone number format.")
        return False, name

    if name in contacts:
        print("The name already exists.")
        return False, name
    
    if phone in contacts.values():
        print(f"The phone number '{phone}' already exists.")
        return False, name

    return True, name

def add_contact(args, contacts, list_contacts):
    if len(args) != 2:
        return "Please provide both name and phone number."
    
    name, phone = args
    is_valid, name = validate_contact(name, phone, contacts)

    if is_valid:
        contacts[name] = phone
        list_contacts.append({name: phone})
        return "Contact added."
    return "Contact doesn't add."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Please provide both name and new phone number."
    
    name, new_phone = args
    name = name.lower()

    if not is_valid_phone(new_phone):
        return "You entered an incorrect phone."

    if name in contacts and new_phone != contacts[name]:
        answer = input("Do you really want to change the number of an existing contact? (y/n) ").strip().lower()
        if answer in ["y", "yes"]:
            contacts[name] = new_phone
            return "Contact changed."
        return "Number doesn't change."
    

def all_contacts(list_contacts):
    if not list_contacts:
        print("No contacts found.")
    else:
        for contact in list_contacts:
            print(contact)

def main():
    contacts = {}
    list_contacts = []
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts, list_contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all" and not args:
            all_contacts(list_contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
