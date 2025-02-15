from unittest import TestCase
from Source.ClassCostume import Costume


class TestCostume(TestCase):

    def test_costume_main_color(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.assertEqual(self.costume.costume_name,"Bad guy")

    def test_costume_material(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.assertEqual(self.costume.costume_material, "cotton")

    def test_costume_name(self):
        self.costume = Costume(costume_name="Bad guy", costume_material="cotton",
                               costume_main_color="gray")
        self.assertEqual(self.costume.costume_main_color, "gray")
