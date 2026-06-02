from enum import Enum, IntEnum, auto

class RoomStatus(Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    OCCUPIED = "occupied"
    MAINTENANCE = "maintenance"

class RoomType(Enum):
    SINGLE = "single"
    DOUBLE = "double"
    SUITE = "suite"
    DELUXE = "deluxe"

    def price(self):
        RoomType.SINGLE = 10
        RoomType.DOUBLE = 20
        RoomType.SUITE = 30
        RoomType.DELUXE = 40


class ReservationStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CHECKED_IN = "checked_in"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

