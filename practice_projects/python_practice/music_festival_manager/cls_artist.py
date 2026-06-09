from enum import Enum, IntEnum
import enums as e

# Step 3 — Build the Artist dataclass
# Attributes: name, artist_id, genre, stage_requirement (a StageSize). Add __post_init__ validation, __eq__, __lt__ (so artists can be sorted by name), a to_dict method, and a from_dict classmethod.

class Artist:
    def __init__(self, name, artist_id, genre:e.Genre, stage_requirement:e.StageSize):
        self.name = name
        self.artist_id = artist_id
        self.genre = genre
        self.stage_requirement = stage_requirement


    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Artist name cannot be empty")
        if not isinstance(self.stage_requirement, e.StageSize):
            raise ValueError(f"{self.stage_requirement} is not a valid stage requirement")
        if not isinstance(self.genre, e.Genre):
            raise ValueError(f"{self.genre} is not a valid genre")

    def __eq__(self, other):
        if not isinstance(other, Artist):
            return False
        return self.artist_id == self.other


    def __lt__(self, other):
        if not isinstance(other, Artist):
            raise NotImplemented
        return self.name < other.name


    def to_dict(self):
        return {
            "Name": self.name,
            "Artist ID" : self.artist_id,
            "Genre": self.genre.to_json(),
            "Stage Requirement": self.stage_requirement.to_json()
        }

    @classmethod
    def from_dict(cls, data:dict)->"Artist":
        """Rebuild an Artist object from a saved dictionary."""
        return cls(
            name = data["name"],
            artist_id = data["artist_id"],
            genre = e.Genre(data["genre"]),
            stage_requirements = e.StageSize(data["stage_requirement"])
        )


    def __str__(self):
        return (f"Artist Name: {self.name} | "
                f"Artist ID: {self.artist_id} | "
                f"Genre: {self.genre.value} | "
                f"Stage Requirement: {self.stage_requirement.value} | "
                f"Stage Capacity: {self.stage_requirement.capacity} | "
               )