from unittest import TestCase
from Source.ClassPerson import Person
from Source.ClassTicket import Ticket
from Source.ClassVisitor import Visitor
from Source.ClassDecoration import Decoration
from Source.ClassScene import Scene

class TestScene(TestCase):

    def test_decorations(self):
        self.ticket = Ticket(ticket_price=100, sit_in_auditorium=12, performance_name="Christmas")
        tickets = [self.ticket]
        self.visitor = Visitor(name="Alex", age=23, have_tickets=tickets)
        visitors = [self.visitor]
        self.decoration = Decoration(decoration_name="Tree", decoration_kind="Forest")
        decorations = [self.decoration]
        self.scene = Scene(decorations = decorations, invited_visitors = visitors)
        self.assertEqual(self.scene.decorations, decorations)

    def test_add_decoration(self):
        self.ticket = Ticket(ticket_price=100, sit_in_auditorium=12, performance_name="Christmas")
        tickets = [self.ticket]
        self.visitor = Visitor(name="Alex", age=23, have_tickets=tickets)
        visitors = [self.visitor]
        self.decoration = Decoration(decoration_name="Tree", decoration_kind="Forest")
        self.new_decoration = Decoration(decoration_name="Bush", decoration_kind="Forest")
        decorations = [self.decoration]
        self.scene = Scene(decorations=decorations, invited_visitors=visitors)
        self.scene.add_decoration(new_decoration = self.new_decoration)
        self.assertEqual(len(self.scene.decorations), 2)

    def test_invite_visitor_to_stage(self):
        self.ticket = Ticket(ticket_price=100, sit_in_auditorium=12, performance_name="Christmas")
        tickets = [self.ticket]
        self.visitor = Visitor(name="Alex", age=23, have_tickets=tickets)
        self.new_visitor = Visitor(name="Al", age=24, have_tickets=tickets)
        visitors = [self.visitor]
        self.decoration = Decoration(decoration_name="Tree", decoration_kind="Forest")
        decorations = [self.decoration]
        self.scene = Scene(decorations=decorations, invited_visitors=visitors)
        self.scene.invite_visitor_to_stage(visitor = self.new_visitor)
        self.assertEqual(len(self.scene.invited_visitors), 2)
