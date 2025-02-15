from Source.ClassCostume import Costume

class CostumeDepartment:

    def __init__(self, *, size: int = 20, costumes: list[Costume]) -> None:
        self.__size = size
        self.__costumes = costumes

    @property
    def size(self) -> int:
        return self.__size

    @property
    def costumes(self) -> list[Costume]:
        return self.__costumes

    @costumes.setter
    def costumes(self, *, costumes: list[Costume]) -> None:
        self.__costumes = costumes

    def create_costume(self, *, costume_main_color: str, costume_material: str, costume_name: str) -> None:
        new_costume = Costume(costume_main_color = costume_main_color,
                              costume_material = costume_material,
                              costume_name = costume_name)
        self.costumes.append(new_costume)

    def costume_amount(self) -> int:
        return len(self.costumes)

    def is_costume_for_role(self, *, necessary_costume_name: str) -> bool:
        is_costume = False
        for costume in self.costumes:
            if costume.costume_name == necessary_costume_name:
                is_costume = True
                return is_costume
        return is_costume

    def costumes_for_performance(self, *, costume_names: list[str]) -> list[Costume]:
        necessary_costumes = []
        for costume in self.costumes:
            if costume.costume_name in costume_names:
                necessary_costumes.append(costume)
        return necessary_costumes
