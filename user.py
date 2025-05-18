from email import Email
from age import Age


class User:
    id = 1

    def __init__(self, name: str, email, age):
        self.id = self._id_generate()
        self.name = self.validate(name)
        self.email = Email(email)
        self.age = Age(age)

    @classmethod
    def _id_generate(cls):
        id = cls.id
        cls.id += 1
        return id

    def get_id(self):
        return self.id

    def validate(self, name) -> str:
        return name.strip().title()

    def get_name(self):
        return self.name

    def change_name(self, name):
        self.name = self.validate(name)

    def get_email(self):
        return self.email

    def change_email(self, email):
        self.email = Email(email)

    def get_age(self):
        return self.age

    def change_age(self, age):
        self.age = Age(age)

    def __str__(self):
        return f"Código do usuário: {self.id}, " \
               f"Nome: {self.name}, " \
               f"Email: {self.email}, " \
               f"Idade: {self.age}"


