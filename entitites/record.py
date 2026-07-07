from entitites.name import Name
from entitites.phone import Phone


class Record:
    def __init__(self, name):
        self.name: Name = Name(name)
        self.phones: list[Phone] = []

    def find_phone(self, phone: str):
        phones = [p for p in self.phones if str(p) == phone]
        return phones[0] if len(phones) > 0 else None

    def add_phone(self, phone):
        created = Phone(phone)
        self.phones.append(created)

    def edit_phone(self, old_phone: str, new_phone):
        self.add_phone(new_phone)
        self.remove_phone(old_phone)

    def remove_phone(self, phone):
        phone = self.find_phone(phone)
        if phone:
            return self.phones.remove(phone)
        raise ValueError("Phone not found")

    def __str__(self):
        return f"{self.name}: {', '.join(str(phone) for phone in self.phones)}"
