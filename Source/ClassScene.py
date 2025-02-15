from Source.ClassDecoration import Decoration
from Source.ClassVisitor import Visitor

class Scene:

    def __init__(self, *, decorations: list[Decoration], invited_visitors: list[Visitor]) -> None:
        self.__decorations = decorations
        self.invited_visitors = []

    @property
    def decorations(self) -> list[Decoration]:
        return self.__decorations

    def add_decoration(self, *, new_decoration: Decoration):
        self.__decorations.append(new_decoration)

    def invite_visitor_to_stage(self, *, visitor: Visitor):
        self.invited_visitors.append(visitor)