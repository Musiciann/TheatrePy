from unittest import TestCase
from Source.ClassPerson import Person
from Source.ClassTicket import Ticket
from Source.ClassVisitor import Visitor
from Source.ClassAuditorium import Auditorium


class TestAuditorium(TestCase):

    def test_visitors(self):
        self.ticket = Ticket(ticket_price=100, sit_in_auditorium=12, performance_name="Christmas")
        tickets = [self.ticket]
        self.visitor = Visitor(name="Alex", age=23, have_tickets=tickets)
        visitors = [self.visitor]
        sits = {1, 2}
        self.auditorium = Auditorium(visitors = visitors, sits = sits)
        self.assertEqual(self.auditorium.visitors, visitors)

    def test_take_sit(self):
        self.ticket = Ticket(ticket_price=100, sit_in_auditorium=12, performance_name="Christmas")
        tickets = [self.ticket]
        self.visitor = Visitor(name="Alex", age=23, have_tickets=tickets)
        self.new_visitor = Visitor(name="Al", age=28, have_tickets=tickets)
        visitors = [self.visitor]
        sits = {1, 2}
        self.auditorium = Auditorium(visitors=visitors, sits=sits)
        self.assertEqual(self.auditorium.take_sit(visitor = self.new_visitor, sit_number = 2), True)

