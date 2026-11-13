class Patient:
    def __init__(self, name):
        self.name = name

class Doctor:
    def __init__(self, name):
        self.name = name

    def treat(self, patient):
        print(f"Dr. {self.name} is treating {patient.name}.")

doc = Doctor("Smith")
pat = Patient("John")