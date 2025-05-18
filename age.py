class Age:

    def __init__(self, age):
        self.age = self.validate(age)

    def validate(self, age) -> int:
        if not age > 0 and age <= 120:
            raise Exception("Idade inválida")
        return age

    def __str__(self):
        return f'{self.age}'
