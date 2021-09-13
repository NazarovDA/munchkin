from curse import Curse
from classes import Class 
from race import Race

races = [
    Race(name="Dwarf", id="M1.D02"),
    Race(name="Dwarf", id="M1.D07"),
    Race(name="Dwarf", id="M1.D09"),
    Race(name="Elf", id="M1.D04"),
    Race(name="Elf", id="M1.D06"),
    Race(name="Elf", id="M1.D08"),
    Race(name="Halfling", id="M1.D10"),
    Race(name="Halfling", id="M1.D11"),
    Race(name="Halfling", id="M1.D13")
]

classes = [
    Class(name="Thief", id="M1.D15"),
    Class(name="Thief", id="M1.D17"),
    Class(name="Thief", id="M1.D19"),
    Class(name="Warrior", id="M1.D12"),
    Class(name="Warrior", id="M1.D14"),
    Class(name="Warrior", id="M1.D16"),
    Class(name="Wizard", id="M1.D18"),
    Class(name="Wizard", id="M1.D20"),
    Class(name="Wizard", id="M1.D21"),
    Class(name="Cleric", id="M1.D01"), 
    Class(name="Cleric", id="M1.D03"), 
    Class(name="Cleric", id="M1.D05"),
]

curses = [
    Curse(
        name="The Duck of doom",
        id="M1.D22",
        effect="lost_lvl",
        value=2
    ),
    Curse(
        name="Class_Change",
        id="M1.D23",
        effect="drop_and_append_class",
        value=None
    ),
    Curse(
        name="Taxes",
        id="M1.D24",
        effect="taxes",
        value=None
    ),
    Curse(
        name="Change Race",
        id="M1.D25",
        effect="drop_and_append_race",
        value=None
    ),
    Curse(
        name="Lost 1 big item",
        id="M1.D26",
        effect="lost_big_item",
        value=1
    ),
    Curse(
        name="Change Sex",
        id="M1.D27",
        effect="change_sex",
        value=-5
    ),
    Curse(
        name="Lose 1 level",
        id="M1.D28",
        effect="lose_level",
        value=-1
    ),
    Curse(
        name="Chicken on your head",
        id="M1.D29",
        effect="change_sex",
        value=-5
    ),
]

__TREASURES__ = []
__DOORS__ = [*classes, *curses, *races]