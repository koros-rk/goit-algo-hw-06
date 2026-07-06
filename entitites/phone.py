import re

from entitites.field import Field


class Phone(Field):
    def __init__(self, value: str):

        if len(value) != 10 or not value.isnumeric():
            raise ValueError("Invalid phone number format")
        super().__init__(value)
