class Costume:

    def __init__(self, *, costume_main_color: str, costume_material: str, costume_name: str) -> None:
        self.__costume_main_color = costume_main_color
        self.__costume_material = costume_material
        self.__costume_name = costume_name

    @property
    def costume_main_color(self) -> str:
        return self.__costume_main_color

    @property
    def costume_material(self) -> str:
        return self.__costume_material

    @property
    def costume_name(self) -> str:
        return self.__costume_name