class Decoration:

    def __init__(self, *, decoration_name: str, decoration_kind: str) -> None:
        self.__decoration_kind = decoration_kind
        self.__decoration_name = decoration_name

    def __str__(self) -> str:
        return f"{self.decoration_name}, {self.decoration_kind}"

    @property
    def decoration_name(self) -> str:
        return self.__decoration_name

    @property
    def decoration_kind(self) -> str:
        return self.__decoration_kind