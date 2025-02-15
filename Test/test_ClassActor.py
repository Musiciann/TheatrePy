from unittest import TestCase
from Source.ClassCostume import Costume
from  Source.ClassPerson import Person
from Source.ClassActor import Actor

class TestActor(TestCase):

    def test_actor_costume(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.actor = Actor(actor_name="Alex", actor_age=23, actor_costume=self.costume, actor_role="main role")
        self.assertEqual(self.actor.actor_costume, self.costume)

    def test_actor_name(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.actor = Actor(actor_name="Alex", actor_age=23, actor_costume=self.costume, actor_role="main role")
        self.assertEqual(self.actor.person_name, "Alex")

    def test_actor_role(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.actor = Actor(actor_name="Alex", actor_age=23, actor_costume=self.costume, actor_role="main role")
        self.assertEqual(self.actor.actor_role, "main role")

    def test_actor_age(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.actor = Actor(actor_name="Alex", actor_age=23, actor_costume=self.costume, actor_role="main role")
        self.assertEqual(self.actor.person_age, 23)

    def test_change_theatrical_character(self):
        self.old_costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.old_costume = Costume(costume_name="Chill guy", costume_material="cotton",
                                   costume_main_color="green")
        self.actor = Actor(actor_name="Alex", actor_age=23, actor_costume=self.costume, actor_role="main role")
        self.assertEqual(self.actor.person_name, "Alex")
