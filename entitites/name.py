from entitites.field import Field


class Name(Field):
    def __init__(self, value):
        if len(value) == 0:
            raise ValueError("Name cannot be empty")
        self.value = value.title()
        super().__init__(value)
