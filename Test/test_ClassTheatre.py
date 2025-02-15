from unittest import TestCase
from Source.ClassTheatre import Theatre
from Source.ClassTicket import Ticket


class TestTheatre(TestCase):

    def test_theatre_name(self):
        self.theatre = Theatre(theatre_name = "Great Theatre", tickets = [])
        self.assertEqual(self.theatre.theatre_name, "Great Theatre")

    def test_tickets(self):
        self.theatre = Theatre(theatre_name="Great Theatre", tickets=[])
        self.assertEqual(bool(self.theatre.tickets), 0)

    def test_add_tickets(self):
        self.ticket_12 = Ticket(ticket_price=100, sit_in_auditorium=12, performance_name="Christmas")
        self.ticket_13 = Ticket(ticket_price=100, sit_in_auditorium=13, performance_name="Christmas")
        current_tickets = [self.ticket_12]
        self.theatre = Theatre(theatre_name="Great Theatre", tickets=current_tickets)
        self.theatre.tickets.append(self.ticket_13)
        self.assertEqual(len(self.theatre.tickets), 2)
