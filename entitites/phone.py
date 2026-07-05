import re

from entitites.field import Field


class Phone(Field):
    def __init__(self, value):
        phone_pattern = re.compile(
            r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        )

        if len(value) < 10 or not phone_pattern.match(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)
