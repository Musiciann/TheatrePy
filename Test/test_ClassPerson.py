from unittest import TestCase
from Source.ClassPerson import Person


class TestPersonInit(TestCase):
    def test_person_name(self):
        self.person = Person(person_name = "Alex", person_age = 22)
        self.assertEqual(self.person.person_name, "Alex")

    def test_person_age(self):
        self.person = Person(person_name="Alex", person_age=22)
        self.assertEqual(self.person.person_age, 22)
