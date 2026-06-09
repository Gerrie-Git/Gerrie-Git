🎵 Intermediate Python Practice Project: Music Festival Manager

📋 Project Overview
Build a Music Festival Management System that manages artists, stages, and performance slots — and saves everything to JSON so your festival persists between runs. This project goes deeper on classes and enums while introducing file handling. You'll practice:

Enum & IntEnum — for genre, performance status, ticket tier, and stage size
Enum methods & properties — with JSON serialisation built in
Deeper class design — __post_init__, __eq__, __lt__ for sorting, class methods
classmethod — for building objects back from saved JSON data
File handling — saving and loading the full festival state with json
Dataclasses — with validation in __post_init__


🗺️ Step-by-Step Plan

Step 1 — Set up Enums
Define Genre (ROCK, POP, JAZZ, ELECTRONIC, HIPHOP), StageSize (SMALL, MEDIUM, LARGE, MAINSTAGE) with a capacity property, PerformanceStatus (SCHEDULED, LIVE, COMPLETED, CANCELLED), and TicketTier (using IntEnum) with a price property.

Step 2 — Add serialisation to Enums
Give each enum a to_json method that returns its value as a string, so enums can be saved cleanly to JSON.

Step 3 — Build the Artist dataclass
Attributes: name, artist_id, genre, stage_requirement (a StageSize). Add __post_init__ validation, __eq__, __lt__ (so artists can be sorted by name), a to_dict method, and a from_dict classmethod.

Step 4 — Build the Slot dataclass
Attributes: slot_id, artist, stage_size, day, start_time, status. Add to_dict and from_dict. Add a method advance_status for valid transitions.
Step 5 — Build the Festival class
The controller. Holds artists and slots. Methods: add_artist, book_slot, update_slot, lineup report, save_to_json, and load_from_json.

Step 6 — Build the TicketOffice class
Separate class that manages ticket sales. Holds a count per TicketTier. Methods: sell_tickets, revenue_report, to_dict, from_dict.

Step 7 — Wire it all together
A demo that builds a festival, books slots, sells tickets, saves to JSON, reloads from JSON, and proves the state was preserved.