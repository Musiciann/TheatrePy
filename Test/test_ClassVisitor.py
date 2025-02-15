from unittest import TestCase
from Source.ClassPerson import Person
from Source.ClassTicket import Ticket
from Source.ClassTheatre import Theatre
from Source.ClassVisitor import Visitor

class TestVisitor(TestCase):

    def test_have_tickets(self):
        self.ticket = Ticket(ticket_price=100, sit_in_auditorium=12, performance_name="Christmas")
        tickets = [self.ticket]
        self.visitor = Visitor(name = "Alex", age = 23, have_tickets = tickets)
        self.assertEqual(self.visitor.have_tickets, tickets)

    def test_buy_ticket(self):
        self.ticket = Ticket(ticket_price=100, sit_in_auditorium=12, performance_name="Christmas")
        self.new_ticket = Ticket(ticket_price=100, sit_in_auditorium=13, performance_name="Christmas")
        current_tickets = [self.ticket]
        self.theatre = Theatre(theatre_name="Great Theatre", tickets=current_tickets)
        tickets = [self.ticket]
        self.visitor = Visitor(name="Alex", age=23, have_tickets=tickets)
        self.visitor.buy_ticket(theatre = self.theatre, performance_name = "Christmas",
                                ticket_sit_number = 13)
        self.assertEqual(len(self.visitor.have_tickets), 2)


