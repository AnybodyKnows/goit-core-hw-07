from AddrBook import * 



john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday("15.01.2023")

print(john_record)






# # Створення нової адресної книги
# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(f" {record}")

# # Знаходження та редагування телефону для John
# john = book.find("John")
# print (john)

# john.edit_phone("1234567890", "1112223333")
# print (john)


# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name.value}: {found_phone}")  

# # Видалення запису Jane
# book.delete("Jane")

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(f"{record}")