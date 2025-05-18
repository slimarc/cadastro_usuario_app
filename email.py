import re


class Email:
    def __init__(self, adress):
        self.email = self.validate(adress)

    def validate(self, adress: str) -> str:
        normalized = adress.strip().lower()
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, normalized):
            raise ValueError("Email inválido")
        return normalized

    def __str__(self):
        return f'{self.email}'

