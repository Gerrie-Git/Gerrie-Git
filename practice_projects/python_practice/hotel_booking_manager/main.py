from enum import Enum, IntEnum, auto
import enums as e


class Room:
    for x in e.RoomType:
        print(x)
    def __init__(self, room_number, room_type, price:e.RoomType.price):
        self.room_number = room_number
        if not isinstance(room_type, e.RoomType):
            raise ValueError(f"{room_type} is not a valid room type")
        else:
            self.room_type = room_type

        self.price = price
        print(self.price)
        self.status = e.RoomStatus.AVAILABLE

    def reserve(self):
        if self.status == e.RoomStatus.AVAILABLE:
            self.status = e.RoomStatus.RESERVED
            return True
        else:
            return False

    def check_in(self):
        if self.status == e.RoomStatus.RESERVED:
            self.status = e.RoomStatus.OCCUPIED
            return True
        else:
            return False

    def check_out(self):
        if self.status == e.RoomStatus.OCCUPIED:
            self.status = e.RoomStatus.AVAILABLE
            return True
        else:
            return False

    def set_maintenance(self):
        self.status = e.RoomStatus.MAINTENANCE

    def __str__(self):
        return(f"Room Number: {self.room_number} |"
               f"Room Type: {self.room_type} |"
               f"Room Price: {self.price} |"
               f"Room Status: {self.status}")


class Guest:
    def __init__(self, name, email, guest_id):
        self.name = name
        self.email = email
        self.guest_id = guest_id

class Reservation:
    def __init__(self, reservation_id, guest, room, check_in_date, check_out_date, status=e.ReservationStatus.PENDING):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = status

    def confirm(self):
        self.status = e.ReservationStatus.CONFIRMED

    def cancel(self):
        self.status = e.ReservationStatus.CANCELLED

    def complete(self):
        self.status = e.ReservationStatus.COMPLETED

    def __str__(self):
        checked_in = self.check_in_date if e.RoomStatus.OCCUPIED else "Not checked in yet"
        checked_out = self.check_out_date 
        return (f"RESERVATION ID: {self.reservation_id} | "
                f"GUEST: {self.guest} | "
                f"ROOM: {self.room} | "
                f"CHECK-IN DATE: {checked_in} | "
                f"CHECK-OUT DATE: {checked_out} |")

class HotelManager:
    def __init__(self):
        self

    def search_available_rooms(self):
        for room in Room:
            if Room.status == "AVAILABLE":
                print(room)


      
Room1 = Room(1, e.RoomType.SINGLE, 10)
print(Room1)
