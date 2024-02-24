
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

# @input_error
def add_contact(command, *args):
    if args[0] in book:
        return f"{args[0]} has been added already"
    else:
        record = Record(args[0])
        record.add_phone(args[1])
        book.add_record(record)
        print(book)


# @input_error
def change_contact(command, *args):
    record = Record(args[0])
    record.add_phone(args[1])
    book.delete(args[0])
    book.add_record(record)
    print(book)

# @input_error
def show_phone(command, *args):
    print(book[args[0]])


# @input_error
def show_all(command, *args):
    for record in book.data.items():
        print(f"{record}")

# @input_error
def show_birthday(*args):
    record = book[args[0]]
    return str(record.birthday.value)

def add_birthday(*args):
    record = book[args[0]]
    book.delete(args[0])
    record.add_birthday(args[1])
    book.add_record(record)
    print(book) 

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
            add_contact(command, *args)
        elif command in ["change"]:
            result = change_contact(command, *args)
            
        elif command in ["phone"]:
            result = show_phone(command, *args)
            print(result)
        elif command in ["all"]:
            show_all(command, *args)
            
        elif command == "add-birthday":
            add_birthday(*args)
        
        elif command == "show-birthday":
            b_day = show_birthday(*args)
            if b_day is None:
                pass
            else:
                print(b_day)
        
        elif command == "birthdays":
            congrat_list = book.get_birthdays(7)
            print(congrat_list)
        
        else:
            print("Invalid comand")              
                
        
if __name__ == "__main__":
     main()



#     test_cmd = """
# add jon 1234567890
# add bob 5555555555
# add sonia 9876543210
# change jon 2222222222
# phone jon
# add-birthday jon 23.04.2000
# add-birthday sonia 28.02.2000
# show-birthday jon
# birthdays"""
#     a = test_cmd.split("\n")
#     print (a)

