from enum import Enum, IntEnum, auto

class TrainStatus(Enum):
    AT_STATION = "at_station"
    BOARDING = "boarding"
    DEPARTED = "departed"
    DELAYED = "delayed"
    CANCELLED = "cancelled"

class TicketClass(Enum):
    STANDARD = "standard"
    FIRST_CLASS = "first_class"
    SLEEPER = "sleeper"

    def PriceMultiplier(self):
        TicketClass.STANDARD = 1.0
        TicketClass.FIRST_CLASS = 1.5
        TicketClass.SLEEPER = 2.0

    def LoungeAccess(self):
        TicketClass.STANDARD = False
        TicketClass.FIRST_CLASS = True
        TicketClass.SLEEPER = True

class RouteStatus(Enum):
    ON_TIME = "on_time"
    DELAYED = "delayed"
    CANCELLED = "cancelled"

class DelaySeverity(IntEnum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

    @property
    def label(self)->str:
        return {DelaySeverity.LOW:      "🟢 LOW",
                DelaySeverity.MEDIUM:   "🟡 MEDIUM",
                DelaySeverity.HIGH:     "🟠 HIGH",
                DelaySeverity.CRITICAL: "🔴 CRITICAL",
        }[self]

    def compensation_percent(self):
        DelaySeverity.LOW = 0.2
        DelaySeverity.MEDIUM = 0.4
        DelaySeverity.HIGH = 0.6
        DelaySeverity.CRITICAL = 0.8