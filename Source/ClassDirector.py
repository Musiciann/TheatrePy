from Source.ClassPerson import Person
from Source.ClassPerformance import Performance
from Source.ClassActor import Actor
from Source.ClassTicket import Ticket
from Source.ClassDecoration import Decoration

class Director(Person):

    def __init__(self, *, name: str, age: int, experience_year: int, performances: list[Performance]) -> None:
        super().__init__(person_name=name, person_age=age)
        self.__experience_year = experience_year
        self.__performances = performances

    @property
    def experience_year(self) -> int:
        return self.__experience_year

    @property
    def performances(self) -> list[Performance]:
        return self.__performances

    def make_performance(self, *, necessary_actor: list[Actor], necessary_decorations: list[Decoration],
                         new_performance_name: str) -> None:
        new_performance = Performance(performance_name = new_performance_name,
                                      necessary_actors = necessary_actor,
                                      necessary_decorations = necessary_decorations)
        self.__performances.append(new_performance)
