def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Contact [{name}] is present. You can change it by command 'change'"
    else:
        contacts[name] = phone
        return f"Contact [{name}] [{phone}] added."

def change_contact(args, contacts):
    name, phone = args
    if contacts.get(name) == None:
        return f"No name in phone books. You can added name by command 'add'"
    else:
        contacts[name] = phone
        return f"Contact [{name}] [{phone}] changed."
        
        
def show_phone(args, contacts):
    name = args[0]
    if contacts.get(name) == None:
        return "No name in phone books"
    else:
        return f"Phone number '{name}' is: '{contacts.get(name)}'"

def show_all(contacts):
    return contacts
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    commands = ["hello", "add", "change", "phone", "all", "close", "exit"]
    while True:
        user_input = input(f"Enter a command ({commands}): \n>>> ")
        command, *args = parse_input(user_input)

        if command in [commands [5], commands [6]]: #["close", "exit"]:
            print("Good bye!")
            break

        elif command == commands [0]: # "hello":
            print("How can I help you?")
        
        elif command == commands [1]: # "add":
            if len(args) == 2:
                print(add_contact(args, contacts))
            else:
                print ("bad command. Enter a command ('add [name] [phone_numder]')")
        
        elif command == commands [2]: # "change":
            if len(args) == 2:
                print(change_contact(args, contacts))
            else:
                print ("bad command. Enter a command ('change [name] [phone_numder]')")  
                
        
        elif command == commands [3]: # "phone":
            if len(args) == 1:
                print(show_phone(args, contacts))
            else:
                print ("bad command. Enter a command ('phone [name]')")
            

        elif command == commands [4]: # "all":
            print(show_all(contacts))
            
                    
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
