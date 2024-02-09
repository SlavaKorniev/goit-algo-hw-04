def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact [{name}] [{phone}] added."

def change_contact(args, contacts):
    name, phone = args
    if contacts.get(name) == None:
        return print(f"No name in phone books. You can added name by command 'add'")
    else:
        y_n_input = None
        while y_n_input != "y" and "n":
            y_n_input = input(f"A you realy want change Phone number '{name}' : '{contacts.get(name)}' on '{phone}'?  (Y/N)\n>>> ").lower()
            if y_n_input == "y":
                contacts[name] = phone
                return print(f"Contact [{name}] [{phone}] changed.")
            elif y_n_input.lower() == "n":
                return print(f"Addition contact [{name}] [{phone}] canceled.")
            print ("Invalid command.")
        
def show_phone(args, contacts):
    name = args[0]
    if contacts.get(name) == None:
        print ("No name in phone books")
    else:
        print (f"Phone number '{name}' is: '{contacts.get(args[0])}'")

def show_all(contacts):
    print (contacts)
    
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
                change_contact(args, contacts)
            else:
                print ("bad command. Enter a command ('change [name] [phone_numder]')")  
                
        
        elif command == commands [3]: # "phone":
            if len(args) == 1:
                show_phone(args, contacts)
            else:
                print ("bad command. Enter a command ('phone [name]')")
            

        elif command == commands [4]: # "all":
            show_all(contacts)        

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
