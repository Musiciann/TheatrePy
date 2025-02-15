class Ticket:

    def __init__(self, *, ticket_price: int, sit_in_auditorium: int, performance_name: str) -> None:
        self.__ticket_price = ticket_price
        self.__sit_in_auditorium = sit_in_auditorium
        self.__performance_name = performance_name

    def __str__(self) -> str:
        return f"{self.__ticket_price=}, {self.__sit_in_auditorium=}, {self.__performance_name}"

    @property
    def ticket_price(self) -> int:
        return self.__ticket_price

    @property
    def sit_in_auditorium(self) -> int:
        return self.__sit_in_auditorium

    @property
    def performance_name(self) -> str:
        return self.__performance_name

    @ticket_price.setter
    def ticket_price(self, *, ticket_price: int):
        self.__ticket_price = ticket_price