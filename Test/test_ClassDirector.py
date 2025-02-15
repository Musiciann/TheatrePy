from unittest import TestCase
from Source.ClassActor import Actor
from Source.ClassDecoration import Decoration
from Source.ClassCostume import Costume
from Source.ClassPerson import Person
from Source.ClassPerformance import Performance
from Source.ClassTicket import Ticket
from Source.ClassDirector import Director


class TestDirector(TestCase):

    def test_experience_year(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.actor = Actor(actor_name="Alex", actor_age=23, actor_costume=self.costume, actor_role="main role")
        self.decoration = Decoration(decoration_name="Tree", decoration_kind="Forest")
        actors = [self.actor]
        decorations = [self.decoration]
        self.performance = Performance(performance_name="Romeo and Julietta", necessary_actors=actors,
                                       necessary_decorations=decorations)
        performances = [self.performance]
        self.director = Director(name = "Victoria", age = 43, experience_year = 6, performances = performances)
        self.assertEqual(self.director.experience_year, 6)

    def test_performances(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.actor = Actor(actor_name="Alex", actor_age=23, actor_costume=self.costume, actor_role="main role")
        self.decoration = Decoration(decoration_name="Tree", decoration_kind="Forest")
        actors = [self.actor]
        decorations = [self.decoration]
        self.performance = Performance(performance_name="Romeo and Julietta", necessary_actors=actors,
                                       necessary_decorations=decorations)
        performances = [self.performance]
        self.director = Director(name="Victoria", age=43, experience_year=6, performances=performances)
        print(self.director.performances)
        self.assertEqual(self.director.performances, performances)

    def test_make_performance(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.actor = Actor(actor_name="Alex", actor_age=23, actor_costume=self.costume, actor_role="main role")
        self.decoration = Decoration(decoration_name="Tree", decoration_kind="Forest")
        actors = [self.actor]
        decorations = [self.decoration]
        self.performance = Performance(performance_name="Romeo and Julietta", necessary_actors=actors,
                                       necessary_decorations=decorations)
        performances = [self.performance]
        self.director = Director(name="Victoria", age=43, experience_year=6, performances=performances)
        self.director.make_performance(necessary_actor = actors, necessary_decorations = decorations,
                                       new_performance_name = " Romeo 2")
        self.assertEqual(len(self.director.performances), 2)

