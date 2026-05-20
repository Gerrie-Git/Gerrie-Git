from enum import Enum
import enums as e

# Build the Passenger dataclass Attributes: name, passenger_id, ticket_class (a TicketClass enum). Add a property has_lounge_access and __str__.
class Passenger:
    def __init__(self, name:str, passenger_id:int, ticket_class):
        self.name = name
        self.passenger_id = passenger_id
        if not isinstance(ticket_class, e.TicketClass):
            raise ValueError(f"{ticket_class} is not a valid ticket class")
        else:
            self.ticket_class = ticket_class

    def has_lounge_access(self)->bool:
        return e.TicketClass.LoungeAccess[self.ticket_class.name]
    
    def __str__(self):
        has_access = "Yes" if self.has_lounge_access == True else "No"
        return (f"Passenger name: {self.name} | "
                f"Passeger ID: {self.passenger_id} | "
                f"Ticket Class: {self.ticket_class.value} | "
                f"Has Lounge Access: {has_access}")
    
#Build the Route dataclass Attributes: origin, destination, distance_km, base_duration_mins, status (a RouteStatus enum). Add a method ticket_price(ticket_class) that applies the price_multiplier. Add a property is_operational.

class Route:
    def __init__(self, origin:str, destination:str, distance_km:int, base_duration_mins:int, status:e.RouteStatus):
        self.origin = origin
        self.destination = destination
        self.distance_km = distance_km
        self.base_duration_mins = base_duration_mins
        if not isinstance(status, e.RouteStatus):
            raise ValueError(f"{status} is not a valid route status")
        else:
            self.status = status

    # This is not complete yet
    def ticket_price(self, ticket_class):
        price = 10 * e.TicketClass.PriceMultiplier[self.ticket_class.value]
        return price
    
    # This is not complete yet
    @property
    def is_operational(self):
        pass

    def __str__(self):
        return (f"Origin : {self.origin} | "
                f"Destination : {self.destination} | "
                f"Distance : {self.distance_km} | "
                f"Duration : {self.base_duration_mins} | "
                f" Status : {self.status.value}")







Passenger1 = Passenger("Gerrit Fourie", 1, e.TicketClass.STANDARD)
Passenger2 = Passenger("Sarah Lunn", 2, e.TicketClass.FIRST_CLASS)
print(Passenger1)
print(Passenger2)
route1 = Route("Amsterdam","Berlin",500,180,e.RouteStatus.ON_TIME)
print(route1)