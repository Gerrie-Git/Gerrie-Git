import enums as e
import cls_artist as ca
import cls_slot as cs
import json


# Step 5 — Build the Festival class
# The controller. Holds artists and slots. Methods: add_artist, book_slot, update_slot, lineup report, save_to_json, and load_from_json.

class Festival:
    def __init__(self, name, filepath: str = "festival.json"):
        self.name = name
        self.filepath = filepath
        self.artist: dict[int, ca.Artist] = {}
        self.slot: dict[int, cs.Slot] = {}
        self._next_slot_id = 1


    def add_artist(self, artist:ca.Artist):
        self.artist[artist.artist_id] = artist
        print(f"  ✅ Artist added: {artist.name} ({artist.genre.value})")


    def book_slot(self, artist_id: int, stage_size: e.StageSize, day: int, start_time: str) -> None:
        artist = self.artist.get(artist_id)
        if not artist:
            print(f"{artist} not found")
            return
        
        for slot in self.slot.values():
            if (slot.day == day and slot.start_time == start_time and slot.stage_size == stage_size):
                print(f"{slot.artist.name} has already been booked")
                return 
        
        try:
            slot = cs.Slot(1, artist, stage_size, day, start_time)
        except ValueError as e:
            print(f"  ❌ Booking failed: {e}")
            return
        
        self.slot[self._next_slot_id] = slot
        self._next_slot_id += 1
        print(f"  📅 Booked: {artist.name} | Day {day} {start_time} "
              f"| {stage_size.value} Stage")
         

    def to_dict(self):
        return {
            "Name" : self.name,
            "Slot ID": self._next_slot_id,
            "Artist": [x.to_dict() for x in self.artist.values()],
            "Slot": [x.to_dict() for x in self.slot.values()]
        }
    
    @classmethod
    def from_dict(cls, data:dict, filepath:str):
        festival = cls(data["name"], filepath)
        festival._next_slot_id = data["next_slot_id"]
        for a in data["artists"]:
            artist = ca.Artist.from_dict(a)
            festival.artists[artist.artist_id] = artist
        for s in data["slots"]:
            slot = cs.Slot.from_dict(s)
            festival.slot[slot.slot_id] = slot
        return festival
    

    def save_to_json(self) -> None:
        with open(self.filepath, "w") as f:
            json.dump(self.to_dict(), f, indent=2)
        print(f"  💾 Festival saved to '{self.filepath}'.")