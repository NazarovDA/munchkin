from door import Door

class Curse(Door):
    def __init__(self, name: str, id: str, effect: str, value: int) -> None:
        super().__init__(id)
        self.name = name
        self.effect = effect
        self.value = value