from entitites.name import Name
from entitites.phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def find_phone(self, phone):
        if phone in self.phones:
            old_phone_index = self.phones.index(phone)
            return self.phones[old_phone_index]
        return None

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        if old_phone not in self.phones:
            raise ValueError("Phone not found")

        old_phone_index = self.phones.index(old_phone)
        self.phones[old_phone_index] = Phone(new_phone)

    def __str__(self):
        return f"{self.name}: {', '.join(str(phone) for phone in self.phones)}"
