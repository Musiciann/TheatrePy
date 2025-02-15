from unittest import TestCase
from Source.ClassActor import Actor
from Source.ClassDecoration import Decoration
from Source.ClassCostume import Costume
from Source.ClassPerformance import Performance

class TestPerformance(TestCase):

    def test_necessary_decorations(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.actor = Actor(actor_name="Alex", actor_age=23, actor_costume=self.costume, actor_role="main role")
        self.decoration = Decoration(decoration_name = "Tree", decoration_kind = "Forest")
        actors = [self.actor]
        decorations = [self.decoration]
        self.performance = Performance(performance_name = "Romeo and Julietta", necessary_actors = actors,
                                       necessary_decorations = decorations)
        self.assertEqual(self.performance.performance_name, "Romeo and Julietta")


    def test_necessary_actors(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.actor = Actor(actor_name="Alex", actor_age=23, actor_costume=self.costume, actor_role="main role")
        self.decoration = Decoration(decoration_name="Tree", decoration_kind="Forest")
        actors = [self.actor]
        decorations = [self.decoration]
        self.performance = Performance(performance_name="Romeo and Julietta", necessary_actors=actors,
                                       necessary_decorations=decorations)
        self.assertEqual(self.performance.necessary_actors, actors)

    def test_performance_name(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.actor = Actor(actor_name="Alex", actor_age=23, actor_costume=self.costume, actor_role="main role")
        self.decoration = Decoration(decoration_name="Tree", decoration_kind="Forest")
        actors = [self.actor]
        decorations = [self.decoration]
        self.performance = Performance(performance_name="Romeo and Julietta", necessary_actors=actors,
                                       necessary_decorations=decorations)
        self.assertEqual(self.performance.necessary_decorations, decorations)

