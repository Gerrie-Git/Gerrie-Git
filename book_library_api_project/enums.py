from enum import Enum

class genres(Enum):
    FICTION = 0
    NONFICTION = 1
    SCIFI = 2
    FANTASY = 3
    MYSTERY = 4

class status(Enum):
    AVAILABLE = 0
    CHECKED_OUT = 1