from unittest import TestCase
from Source.ClassCostume import Costume
from Source.ClassCostumeDepartment import CostumeDepartment

class TestCostumeDepartment(TestCase):

    def test_costume_department_size(self):
        self.costume_department = CostumeDepartment(size=25,costumes=[])
        self.assertEqual(self.costume_department.size, 25)

    def test_costumes_amount_at_start(self):
        self.costume_department = CostumeDepartment(size=25, costumes=[])
        self.assertEqual(bool(self.costume_department.costumes), False)

    def test_create_costume(self):
        self.costume_department = CostumeDepartment(size=25,costumes=[])
        self.costume_department.create_costume(costume_main_color="gray",
                                               costume_name="Christmas",
                                               costume_material="leather")
        self.assertEqual(bool(self.costume_department.costumes), True)

    def test_costume_amount(self):
        self.costume_department = CostumeDepartment(size=25, costumes=[])
        self.assertEqual(self.costume_department.costume_amount(), 0)

    def test_is_costume_for_role(self):
        self.costume_department = CostumeDepartment(size=25, costumes=[])
        self.costume_department.create_costume(costume_main_color="gray",
                                               costume_name="Christmas",
                                               costume_material="leather")
        costume_name = "Christmas"
        self.assertEqual(self.costume_department.is_costume_for_role(necessary_costume_name=costume_name), True)


    def test_costumes_for_performance(self):
        self.costume_department = CostumeDepartment(size=25, costumes=[])
        self.costume_department.create_costume(costume_main_color="gray",
                                               costume_name="Christmas",
                                               costume_material="leather")
        costume_names = ["Christmas"]
        necessary_costumes = self.costume_department.costumes_for_performance(costume_names=costume_names)
        self.assertEqual(necessary_costumes[0].costume_name, costume_names[0])

