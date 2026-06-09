import enums as e
import cls_artist as ac

#Step 4 — Build the Slot dataclass
#Attributes: slot_id, artist, stage_size, day, start_time, status. Add to_dict and from_dict. Add a method advance_status for valid transitions.

class Slot:
    def __init__(self, slot_id, artist:ac.Artist, stage_size:e.StageSize, day, start_time, status:e.PerformanceStatus=e.PerformanceStatus.SCHEDULED):
        self.slot_id = slot_id
        self.artist = artist
        self.stage_size = stage_size
        self.day = day
        self.start_time = start_time
        self.status = status

    def to_dict(self):
        return {
            "slot_id" : self.slot_id,
            "artist" : self.artist,
            "stage_size" : self.stage_size,
            "day" : self.day,
            "start_time" : self.start_time,
            "status" : self.status
        }
    
    @classmethod
    def from_dict(cls, data:dict)->"Slot":
        return cls(
            slot_id = data["slot_id"],
            artist = data["artist"],
            stage_size = e.StageSize(data["stage_size"]),
            day = data["day"],
            start_time = data["start_time"],
            status = data["status"]
        )
    
    def advance_status(self):
        next_s = e.PerformanceStatus.next_status()
        if next_s is None:
            print(f"Slot # {self.slot_id} is already {self.status.name}")
            return
        else:
            self.status = next_s

        return f"{self.artist.name} -> {self.status.name}"
    
    def __str__(self):
        return (f"Slot ID: {self.slot_id} |"
                f"Artist: {self.artist.name} |"
                f"Stage Size: {self.stage_size.value} |"
                f"Day: {self.day} |"
                f"Start time: {self.start_time} |"
        )
    



