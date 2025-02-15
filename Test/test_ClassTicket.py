from unittest import TestCase
from Source.ClassTicket import Ticket


class TestTicket(TestCase):

    def test_ticket_sit(self):
        self.ticket = Ticket(ticket_price = 100, sit_in_auditorium = 12, performance_name = "Christmas")
        self.assertEqual(self.ticket.sit_in_auditorium, 100)

    def test_ticket_price(self):
        self.ticket = Ticket(ticket_price=100, sit_in_auditorium=12, performance_name="Christmas")
        self.assertEqual(self.ticket.ticket_price, 100)

    def test_set_performance_name(self):
        self.ticket = Ticket(ticket_price=100, sit_in_auditorium=12, performance_name="Christmas")
        self.ticket.__performance_name = "Abracadabra"
        self.assertEqual(self.ticket.performance_name, "Abracadabra")

    def test_performance_name(self):
        self.ticket = Ticket(ticket_price=100, sit_in_auditorium=12, performance_name="Christmas")
        self.assertEqual(self.ticket.performance_name, "Christmas")
