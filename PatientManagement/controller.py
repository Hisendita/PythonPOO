from patient import Patient

class Controller:
    def __init__(self):
        self.patients = {}
    
    def add_patient(self, patient):
        if patient.get_nif() in self.patients:
            return False
        
        self.patients[patient.get_nif()] = patient
        return True
    
    def delete_patient(self, nif):
        if nif not in self.patients:
            return False
        del self.patients[nif]
        return True
    
    def get_patient_hov(self, nif):
        if nif not in self.patients:
            return False
        
        return self.patients[nif]
    
    def add_appointment(self, patient, appointment):
        if patient.get_nif() not in self.patients:
            return False
        
        patient.set_hov(appointment)
        patient.set_nov = patient.get_nov() + 1
        return True
    
    def check_nif(self, nif):
        letters = "TRWAGMYFPDXBNJZSQVHLCKE"
        numbers = "1234567890"
        
        if len(nif) == 9:
            letter = nif[8].upper()
            l = nif[:8]
            if len(l) == len([n for n in l if n in numbers]):
                if letters[int(l)%23] == letter:
                    return True
        return False
    
    def getListOfPatients(self):
        return self.patients
    