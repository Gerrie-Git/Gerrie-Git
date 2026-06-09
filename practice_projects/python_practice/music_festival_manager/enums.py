from enum import Enum, IntEnum, auto
import json


class Genre(Enum):
    ROCK = "rock"
    POP = "pop"
    JAZZ = "jazz"
    ELECTRONIC = "electronic"
    HIPHOP = "hiphop"

    def to_json(self)->str:
        return self.value


class StageSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    MAINSTAGE = "mainstage"

    @property
    def capacity(self):
        return {StageSize.SMALL: 1000,
                StageSize.MEDIUM: 2000,
                StageSize.LARGE: 5000,
                StageSize.MAINSTAGE: 10000
        }[self]
    
    def to_json(self)->str:
        return self.value


class PerformanceStatus(Enum):
    SCHEDULED = "scheduled"
    LIVE = "live"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

    def next_status(self):
        flow = {
            PerformanceStatus.SCHEDULED: PerformanceStatus.LIVE,
            PerformanceStatus.LIVE:      PerformanceStatus.COMPLETED,
        }
        return flow.get(self, None)

    def to_json(self)->str:
        return self.value


class TicketTier(IntEnum):
    STANDARD = auto()
    PREMIUM = auto()
    VIP = auto()

    @property
    def price(self):
        return {TicketTier.STANDARD: 100,
                TicketTier.PREMIUM: 150,
                TicketTier.VIP: 200
        }[self]
    
    def to_json(self)->str:
        return self.value


