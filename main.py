from entitites.address_book import AddressBook
from entitites.record import Record


def main():
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("0987654321")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print(book, "\n")

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    try:
        john.edit_phone("0987654321", "11122233asd")
    except ValueError as e:
        print(e)
    john.remove_phone("5555555555")

    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    book.delete("Jane")

    print("\n")


if __name__ == "__main__":
    main()
