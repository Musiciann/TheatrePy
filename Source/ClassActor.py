from Source.ClassPerson import Person
from Source.ClassCostume import Costume

class Actor(Person):

    def __init__(self, *, actor_name: str = "Undefined", actor_age: int = 0, actor_costume: Costume, actor_role: str) -> None:
        super().__init__(person_name = actor_name, person_age = actor_age)
        self.__actor_costume = actor_costume
        self.__actor_role = actor_role

    def __str__(self) -> str:
        return f"{self.person_name=}, {self.person_age}, {self.actor_role}"

    @property
    def actor_costume(self) -> Costume:
        return self.__actor_costume

    @property
    def actor_role(self) -> str:
        return self.__actor_role

    @actor_role.setter
    def actor_role(self, *, actor_role: str) -> None:
        self.__actor_role = actor_role

    @actor_costume.setter
    def actor_costume(self, *, actor_costume: Costume) -> None:
        self.__actor_costume = actor_costume

    def change_theatrical_character(self, *, new_actor_costume: Costume, new_actor_role: str) -> None:
        self.__actor_costume = new_actor_costume
        self.__actor_role = new_actor_role

