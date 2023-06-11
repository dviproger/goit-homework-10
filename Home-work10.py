from collections import UserDict


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data.update({record.name: record.phones})
        
    def search(self):
        pass

class Record():
    def __init__(self, name, phone):
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
    
