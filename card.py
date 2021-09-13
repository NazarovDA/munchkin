class Card:
    def __init__(self, id: str) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"Card {self.id}"