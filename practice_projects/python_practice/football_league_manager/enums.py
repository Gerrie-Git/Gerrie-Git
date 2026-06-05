from enum import Enum, IntEnum


class Position(Enum):
    GOALKEEPER = "goalkeeper"
    DEFENDER = "defender"
    MIDFIELDER = "midfielder"
    FORWARD = "forward"

    @property
    def typical_shirt_number(self):
        return {Position.GOALKEEPER : "10",
        Position.DEFENDER : "4",
        Position.MIDFIELDER : "8",
        Position.FORWARD : "7"
        }[self]

class MatchStatus(Enum):
    SCHEDULED = "scheduled" 
    LIVE = "live"
    COMPLETED = "completed"
    POSTPONED = "postponed"

    @property
    def can_advance(self):
        return {MatchStatus.SCHEDULED : True,
        MatchStatus.LIVE : False,
        MatchStatus.COMPLETED : False,
        MatchStatus.POSTPONED : False
        }[self]

class CardType(Enum):
    YELLOW = "yellow"
    RED = "red"

class Form(IntEnum):
    WIN = 3
    DRAW = 1
    LOSS = 0

    @property
    def points(self) -> int:
        return self.value

    @property
    def label(self)->str:
        return {Form.WIN: "🟢 WIN",
                Form.DRAW: "🟡 DRAW",
                Form.LOSS: "🔴  LOSS"          
        }[self]
    
