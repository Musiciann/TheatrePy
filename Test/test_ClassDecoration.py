from unittest import TestCase
from Source.ClassDecoration import Decoration

class TestDecoration(TestCase):
    def test_decoration_name(self):
        self.decoration = Decoration(decoration_name = "Tree", decoration_kind = "Forest")
        self.assertEqual(self.decoration.decoration_name, "Tree")

    def test_decoration_kind(self):
        self.decoration = Decoration(decoration_name="Tree", decoration_kind="Forest")
        self.assertEqual(self.decoration.decoration_kind, "Forest")
