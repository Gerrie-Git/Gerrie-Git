from enum import Enum, IntEnum

class MissionPhase(Enum):
    PLANNING = "planning"
    LAUNCH = "launch"
    ORBIT = "orbit"
    LANDING = "landing"
    COMPLETE = "complete"

    def next_phase(self):
        phases = list(MissionPhase)
        idx = phases.index(self)
        return phases[idx + 1] if idx + 1 < len(phases) else None

class CrewRole(Enum):
    COMMANDER = "commander"
    PILOT = "pilot"
    SCIENTIST = "scietist"
    ENGINEER = "engineer"

class RocketStatus(Enum):
    READY = 0
    LAUNCHED = 1
    DAMAGED = 2
    DESTROYED = 3

class AlertLevel(IntEnum):
    GREEN = 0
    YELLOW = 1
    ORANGE = 2
    RED = 3

    def color():
        return AlertLevel.value


class CrewMember:
    def __init__(self, name, CrewRole, experience_years):
        self.name = name
        self.role = CrewRole
        self.experience_years = experience_years

    def is_senior(self):
        if self.experience_years >= 5:
            return True
        
    def __str__():
        pass

class Rocket:
    def __init__(self, name, fuel=0):
        self.name = name
        self.fuel = fuel
        self.status = RocketStatus.READY

    def refuel(self, amount):
        self.fuel += amount

    def consume_fuel(self, amount):
        self.fuel -= amount
    
    def take_damage(self, amount):
        self.status.value += amount


class Mission:

    def __init__(self, name, Rocket):
        self.name = name
        self.rocket = Rocket
        self.crew_list = []
        self.mission_phase = MissionPhase.PLANNING
        self.alert_level = AlertLevel.GREEN

    def add_crew(self, CrewMember):
        self.crew_list.append(CrewMember)

    def advance_phase(self)->bool:
        next_p = self.mission_phase.next_phase()

        if next_p is None:
            print(f"Mission already complete")
            return False

        self.mission_phase = next_p
        print(f"Mission phase advanced : {self.mission_phase.name}")
        return True

    def raise_alert(self, next_level):
        self.alert_level = next_level
        print(f"Alert level raised to {self.alert_level.name}")


    def status_report(self):
        print(f"Name: {self.name}")
        print(f"Rocket: {self.rocket.name}")
        print(f"Status: {self.rocket.status}")
    

if __name__ == "__main__":
    # Build rocket and mission
    rocket  = Rocket("Helios-7")
    mission = Mission("Operation Starfall", rocket)

    # Assemble crew
    print("\n── Assembling Crew ──")
    mission.add_crew(CrewMember("Elena Vasquez", CrewRole.COMMANDER,  experience_years=10))
    mission.add_crew(CrewMember("Jin Park",      CrewRole.PILOT,       experience_years=6))
    mission.add_crew(CrewMember("Amir Hassan",   CrewRole.SCIENTIST,   experience_years=3))
    mission.add_crew(CrewMember("Sara Müller",   CrewRole.ENGINEER,    experience_years=8))

    # Initial report
    mission.status_report()

    # Advance through phases
    print("── Phase Progression ──")
    mission.advance_phase()   # PLANNING → LAUNCH
    mission.advance_phase()   # LAUNCH → ORBIT

    # Mid-mission anomaly
    print("\n── Anomaly Detected ──")
    mission.raise_alert(AlertLevel.YELLOW)
    mission.raise_alert(AlertLevel.ORANGE)   # triggers damage

    # Continue mission
    print("\n── Resuming Mission ──")
    mission.advance_phase()   # ORBIT → LANDING
    mission.advance_phase()   # LANDING → COMPLETE

    # Final report
    mission.status_report()

