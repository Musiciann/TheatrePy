from Source.ClassTicket import Ticket

class Theatre:

    def __init__(self, *, theatre_name: str, tickets: list[Ticket]) -> None:
        self.__theatre_name = theatre_name
        self.__tickets = tickets

    @property
    def theatre_name(self) -> str:
        return self.__theatre_name

    @property
    def tickets(self) -> list[Ticket]:
        return self.__tickets

    @tickets.setter
    def tickets(self, *, tickets: list[Ticket]):
        self.tickets = tickets