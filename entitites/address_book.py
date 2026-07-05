from collections import UserDict

from entitites.record import Record


class AddressBook(UserDict[str, Record]):
    def find(self, name: str):
        return self.data.get(name.casefold())

    def add_record(self, record: Record):
        key = record.name.value.casefold()
        self.data.update({key: record})

    def delete(self, name):
        if name in self.data:
            del self.data[name.casefold()]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
