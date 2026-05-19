from enum import Enum, IntEnum

class BloodType(Enum):
    A_POS = "a_pos"
    B_NEG = "b_neg"
    O_POS = "o_pos"
    B_POS = "b_pos"
    AB_POS = "ab_pos"
    A_NEG = "a_neg"

class Department(Enum):
    CARDIOLOGY = "cardiology"
    NEUROLOGY = "neurology"
    EMERGENCY = "emergency"

    def typical_duration_mins(Department):
        # returns the average appointment length per department
        pass
        

class Priority(IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2
    CRITICAL = 4

    def label():
        # returns a coloured display string.
        pass

class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Patient:
    def __init__(self, name, patient_id, bloodtype, priority):
        self.name = name
        self.patient_id = patient_id

        if not isinstance(bloodtype, BloodType):
            raise ValueError(f"{bloodtype} is not a valid blood type")
        else:
            self.bloodtype = bloodtype

        if not isinstance(priority, Priority):
            raise ValueError(f"{priority} is not valid")
        else:    
            self.priority = priority

    def needs_urgent_care(self):
        return self.priority >= Priority.HIGH
         
        
    def __str__(self):
        urgent = "Urgent" if self.needs_urgent_care else self.priority
        return (f"Patient name: {self.name} | "
                f"Patient ID: {self.patient_id} |"
                f"Bloodtype: {self.bloodtype} |"
                f"Priority: {urgent}")
    
class Doctor:
    def __init__(self, name, doctor_id, department, is_available=True):
        self.name = name
        self.doctor_id = doctor_id
        if not isinstance(department, Department):
            raise ValueError(f"{department} is not a valid department")
        else:
            self.department = department
        self.assigned_patient_id = []
        self.is_available = is_available

    def is_available(self)->bool:
        return len(self.assigned_patient_ids) < 5
    
    def __str__(self):
        availability = f"Available" if self.is_available else "Full"
        return (f"Doctor name: {self.name} | "
                f"Doctor ID: {self.doctor_id} |"
                f"Department: {self.department} |"
                f"Assigned patients: {self.assigned_patient_id} |"
                f"Availability: {availability}")

class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.status = AppointmentStatus.SCHEDULED
        
    def __str__(self):
        return (f"Appt [{self.appointment_id}] "
                f"Patient {self.patient_id} → Doctor {self.doctor_id} "
                f"| {self.status.status}")

class Hospital:
    def __init__(self, name):
        self.name = name
        self._patients: dict[int, Patient] = {} 
        self._doctors:  dict[int, Doctor]  = {}
        self._appointments: dict[int, Appointment] = {}
        self.next_appointment_id = 1

    def admit_patient(self, patient:Patient) -> None:
        self._patients[patient.patient_id] = patient
        print(f"  ✅ Admitted : {patient}")
    
    def register_doctor(self, doctor:Doctor) -> None:
        self._doctors[doctor.doctor_id] = doctor
        print(f"  ✅ Admitted : {doctor}")
    
    def schedule_appointment(patient, doctor):
        pass
        
    def update_appointment():
        pass
        
    def status_report(self) -> None:
        print(f"\n{'='*58}")
        print(f"  🏥 {self.name} — Status Report")
        print(f"{'='*58}")

        print(f"\n  👥 Patients ({len(self._patients)}):")
        for p in sorted(self._patients.values(),
                        key=lambda x: x.priority, reverse=True):
            print(f"    {p}")

        print(f"\n  👨‍⚕️  Doctors ({len(self._doctors)}):")
        for d in self._doctors.values():
            print(f"    {d}")

        print(f"\n  📋 Appointments ({len(self._appointments)}):")
        for a in self._appointments.values():
            print(f"    {a}")

        print(f"{'='*58}\n")





if __name__ == "__main__":
    hospital = Hospital("St. Claude's Medical Centre")

    # Admit patients
    print("\n── Admitting Patients ──")
    hospital.admit_patient(Patient("Maria Santos",  1, BloodType.O_POS,  Priority.CRITICAL))
    hospital.admit_patient(Patient("Tom Bergmann",  2, BloodType.A_NEG,  Priority.LOW))
    hospital.admit_patient(Patient("Yuki Tanaka",   3, BloodType.B_POS,  Priority.HIGH))
    hospital.admit_patient(Patient("Fatima Al-Ali", 4, BloodType.AB_POS, Priority.MEDIUM))

    # Register doctors
    print("\n── Registering Doctors ──")
    hospital.register_doctor(Doctor("Chen",    1, Department.EMERGENCY))
    hospital.register_doctor(Doctor("Okafor",  2, Department.CARDIOLOGY))
    hospital.register_doctor(Doctor("Patel",   3, Department.NEUROLOGY))

    # Initial report
    hospital.status_report()

    # Schedule appointments
    #print("── Scheduling Appointments ──")
    #hospital.schedule_appointment(1, 1)   # Maria  → Dr. Chen    (Emergency)
    #hospital.schedule_appointment(3, 1)   # Yuki   → Dr. Chen    (Emergency)
    #hospital.schedule_appointment(2, 2)   # Tom    → Dr. Okafor  (Cardiology)
    #hospital.schedule_appointment(4, 3)   # Fatima → Dr. Patel   (Neurology)

    # Advance appointments
    #print("\n── Updating Appointments ──")
    #hospital.update_appointment(1)            # SCHEDULED → IN_PROGRESS
    #hospital.update_appointment(1)            # IN_PROGRESS → COMPLETED
    #hospital.update_appointment(2)            # SCHEDULED → IN_PROGRESS
    #hospital.update_appointment(3, cancel=True)  # Cancelled

    # Final report
    #hospital.status_report()