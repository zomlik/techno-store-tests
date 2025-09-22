from mimesis import Locale, Person


class FakeData:
    def __init__(self):
        self._person = Person(Locale.RU)

    def first_name(self) -> str:
        return self._person.first_name()

    def last_name(self) -> str:
        return self._person.last_name()

    def email(self) -> str:
        return self._person.email()

    def password(self) -> str:
        return self._person.password()


fake = FakeData()
