from Source.ClassActor import Actor
from Source.ClassDecoration import Decoration

class Performance:

    def __init__(self, *, performance_name: str, necessary_actors: list[Actor],
                 necessary_decorations: list[Decoration]) -> None:
        self.__performance_name = performance_name
        self.__necessary_actors = necessary_actors
        self.__necessary_decorations = necessary_decorations

    @property
    def necessary_decorations(self) -> list[Decoration]:
        return self.__necessary_decorations

    @property
    def necessary_actors(self) -> list[Actor]:
        return self.__necessary_actors

    @property
    def performance_name(self) -> str:
        return self.__performance_name