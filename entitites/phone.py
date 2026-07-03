import re

from entitites.field import Field


class Phone(Field):
    def __init__(self, value):
        if len(value) < 10:
            raise ValueError("Invalid phone number format")
        super().__init__(value)
