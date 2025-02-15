class Person:

    def __init__(self, *, person_name: str = "Undefined", person_age: int = 0) -> None:
        self.__person_name = person_name
        self.__person_age = person_age

    @property
    def person_name(self) -> str:
        return self.__person_name

    @property
    def person_age(self) -> int:
        return self.__person_age

