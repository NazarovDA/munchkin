from door import Door


class Class(Door):
    def __init__(self, name: str, id: str) -> None:
        super().__init__(id)
        self.__name = name

    def get_name(self) -> str:
        return self.__name