from Source.ClassTheatre import Theatre
from Source.ClassPerson import Person
from Source.ClassTicket import Ticket

class Visitor(Person):

    def __init__(self, *, name: str, age: int, have_tickets: list[Ticket]) -> None:
        super().__init__(person_name=name, person_age=age)
        self.__have_tickets = have_tickets

    @property
    def have_tickets(self) -> list[Ticket]:
        return self.__have_tickets

    def buy_ticket(self, *, theatre: Theatre, performance_name: str, ticket_sit_number: int) -> None:
        for ticket in theatre.tickets:
            if ticket.sit_in_auditorium == ticket_sit_number:
                theatre.tickets.remove(ticket)
                self.have_tickets.append(ticket)
            else:
                print(f"Ticket for {performance_name} and {ticket_sit_number} sit number wasn't found")
