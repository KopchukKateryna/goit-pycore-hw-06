from collections import UserDict


class Field:
    """
    A base class for fields in a record.

    Attributes:
        * value (str): The value of the field.
    """
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """
    A class for storing a contact's name.

    Inherits from Field.
    """
    pass


class Phone(Field):
    """
    A class for storing a contact's phone number.

    Inherits from Field. Validates that the phone number is exactly 10 digits.
    """
    def __init__(self, value: str):
        if len(value) != 10:
            raise ValueError("Phone number must be exactly 10 digits.")
        super().__init__(value)


class Record:
    """
    A class for storing contact information, including name and phone numbers.

    Attributes:
        * name (Name): The contact's name.
        * phones (list of Phone): A list of the contact's phone numbers.
    """
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        """
        Adds a phone number to the contact's list of phone numbers.

        Args:
            * phone (str): The phone number to be added.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """
        Removes a phone number from the contact's list of phone numbers.

        Args:
            * phone (str): The phone number to be removed.
        """
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone: str, new_phone: str):
        """
        Edit an existing phone number in the contact's list of phone numbers.

        Args:
            * old_phone (str): The phone number to be replaced.
            * new_phone (str): The new phone number to replace the old one.
        """
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone

    def find_phone(self, phone: str):
        """
        Find a phone number in the contact's list of phone numbers.

        Args:
            * phone (str): The phone number to find.

        Returns:
            * Phone: The phone object if found, None otherwise.
        """
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """
    A class for storing and managing contact records.

    Inherits from UserDict.
    """
    def add_record(self, record: Record):
        """
        Add a contact record to the address book.

        Args:
            * record (Record): The contact record to be added.
        """
        self.data[record.name.value] = record

    def find(self, name: str):
        """
        Find a contact record by name.

        Args:
            * name (str): The name of the contact to find.

        Returns:
            * Record: The contact record if found
        """
        return self.data.get(name)

    def delete(self, name: str):
        """
        Delete a contact record by name.

        Args:
            * name (str): The name of the contact to delete.
        """
        if name in self.data:
            del self.data[name]


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
