from Source.ClassVisitor import Visitor

class Auditorium:

    def __init__(self, *, visitors: list[Visitor], sits: set[int]) -> None:
        self.__visitors = visitors
        self.__sits = {}

    @property
    def visitors(self) -> list[Visitor]:
        return self.__visitors

    def take_sit(self, *, visitor: Visitor, sit_number: int) -> bool:
        could_sit = True
        if sit_number not in self.__sits.keys():
            self.__visitors.append(visitor)
            self.__sits[sit_number] = visitor
            return could_sit
        could_sit = False
        return could_sit