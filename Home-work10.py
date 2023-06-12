from collections import UserDict


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data[record.name.value] = record

    def search(self):
        pass

    def show(self):
        print(f'{self.data}')


class Record():
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = [phone]

    def get_record(self):
        print(f'{self.name} {self.phones}')
        return {self.name.value: self.phones}

    def add_phone(self, phone):
        self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        index_old_phone = self.phones.index(old_phone)
        self.phones[index_old_phone] = new_phone

    def delete(self, phone):
        self.phones.remove(phone)


class Field():
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    # assert isinstance(ab['Bill'], Record)
    # assert isinstance(ab['Bill'].name, Name)
    # assert isinstance(ab['Bill'].phones, list)
    # assert isinstance(ab['Bill'].phones[0], Phone)
    # assert ab['Bill'].phones[0].value == '1234567890'
    # print('All Ok)')
