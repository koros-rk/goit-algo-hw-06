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
        return created

    def edit_phone(self, old_phone: str, new_phone):
        deleted = self.remove_phone(old_phone)
        if deleted:
            return self.add_phone(new_phone)
        return None

    def remove_phone(self, phone):
        phone = self.find_phone(phone)
        if phone:
            self.phones.remove(phone)
            return phone
        return None

    def __str__(self):
        return f"{self.name}: {', '.join(str(phone) for phone in self.phones)}"
