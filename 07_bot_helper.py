
from AddrBook import * 

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Command not Found."
        except KeyError:
            return "Name not Found."
        except Exception as e:
            return f"Error: {e}"
    return inner

book = AddressBook()
contucts_book = []


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args  

@input_error
def add_contact(command, *args):
    if args[0] in book:
        return f"{args[0]} has been added already"
    else:
        record = Record(args[0])
        record.add_phone(args[1])
        book.add_record(record)
        print(book)



@input_error
def change_contact(command, *args):
    if args[0] in contucts_book:
        contucts_book[args[0]] = args[1]
        return ("Contact updated.")
    else: return "No such contuct"

@input_error
def show_phone(command, *args):
    return contucts_book[args[0]]

@input_error
def show_all(command, *args):
    return contucts_book


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input) 
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello"]:
            print("Hello how can I help you?")
        elif command in ["add"]:
            record = Record(args[0])
            record.add_phone(args[1])
            book.add_record(record)
            print(book)
            
        elif command in ["change"]:
            result = change_contact(command, *args)
            print(result)
        elif command in ["phone"]:
            result = show_phone(command, *args)
            print(result)
        elif command in ["all"]:
            result = show_all(command, *args)
            print(result)
        elif command == "add-birthday":
            pass
        
        elif command == "show-birthday":
            pass
        
        elif command == "birthdays":
            pass
        
        else:
            print("Invalid comand")              
                
        
if __name__ == "__main__":
    main()