from patient import Patient
from controller import Controller
from datetime import datetime
import requests, urllib3, json

def get_age(patient):
    yob = patient.get_yob()
    today = datetime.now()
    
    return today.year - yob.year - ((today.month, today.day) < (yob.month, yob.day))

def get_health(patient, weight, height):
    url = "https://fitness-calculator.p.rapidapi.com/bmi"

    querystring = {"age":get_age(patient),"weight":weight,"height":height}

    headers = {
        'x-rapidapi-host': "fitness-calculator.p.rapidapi.com",
        'x-rapidapi-key': "7ab4fc33f3mshb48bea3705add01p16d30fjsnc09d5274bbdc"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = dict(json.loads(response.text))
    
    return data

opc = 0
c = Controller()
nop = 0 # Number Of Patients

while True:
    print("Matias Polyclinic")
    print("Currently there are",nop,"registered patients.")
    print("1.- Add Patient")
    print("2.- Delete Patient")
    print("3.- Get Patient History")
    print("4.- List Patient")
    print("5.- Add Appointment")
    print("6.- Get Health")
    print("7.- Exit")
    
    while True:
        try:
            opc = int(input("Choose option: "))
            if opc > 0 or opc < 7:
                break
        except ValueError:
            print("[ERROR] Input an accepted value.")
            
    if opc == 7:
        print("Bye-bye.")
        break
    
    if opc == 1: # Adding a Patient
        while True:
            nif = input("Input nif:")
            if c.check_nif(nif):
                break
            else:
                print("[ERROR] Input a valid NIF.")
        name = input("Input name:")
        surname = input("Input surname:")
        yob = datetime.strptime(input("Input date of birth:"), "%d/%m/%Y")
        while True:
            try:
                telf = int(input("Input phone:"))
                if len(str(telf)) == 9:
                    break
                else:
                    print("[ERROR] Input an accepted phone number.")
            except ValueError:
                print("[ERROR] Input an accepted phone number.")
        while True:
            mail = input("Input mail:")
            if "@" not in mail:
                print("[ERROR] e-mail format not accepted.")
            elif "@" in mail:
                break
        patient = Patient(nif, name, surname, yob, telf, mail)
        if c.add_patient(patient):
            print("Patient added correctly")
            nop += 1
        else:
            print("[ERROR] Something went wrong.")
    
    if opc == 2: # Deleting a Patient
        while True:
            nif = input("Input nif:")
            if c.check_nif(nif):
                break
            else:
                print("[ERROR] Input a valid NIF.")
        if c.delete_patient(nif):
            print("Patient deleted")
        else:
            print("[ERROR] Something went wrong.")
    
    if opc == 3: # Visualizing a Patient's History of Visits
        while True:
            nif = input("Input nif:")
            if c.check_nif(nif):
                break
            else:
                print("[ERROR] Input a valid NIF.")
        patient = c.get_patient_hov(nif)
        if (patient):
            print("Name:",patient.get_name())
            print("Surname:",patient.get_surname())
            print("Phone:",patient.get_telf())
            print("e-mail:",patient.get_mail())
            print("Number of visits:",patient.get_nov())
            print("History:")
            print("\t"+patient.get_hov())
    if opc == 4: # List patients
            patients = c.getListOfPatients()
            for k,v in patients.items():
                print("Patient DNI", k)
                print("Name", v.get_name())
                print("Name", v.get_name())
                
    
    if opc == 5: # Adding an appointment to a patient
        while True:
            nif = input("Input nif:")
            if c.check_nif(nif):
                break
            else:
                print("[ERROR] Input a valid NIF.")
        patient = c.get_patient_hov(nif)
        if patient:
            now = datetime.now()
            date = now.strftime("%d/%m/%Y %H:%M")
            matter = input("Input visit matter:")
            
            appointment = date + " - " + matter
            
            if c.add_appointment(patient, appointment):
                print("Appointment added")
    if opc == 6: # Get health of a patient
        while True:
            nif = input("Input nif:")
            if c.check_nif(nif):
                break
            else:
                print("[ERROR] Input a valid NIF.")
        patient = c.get_patient_hov(nif)
        if patient:
            height = int(input("Input your height in centimeters: "))
            weight = int(input("Input your weight in kilograms: "))
            data = get_health(patient, weight, height)
            print("BMI of patient:",data["data"]["bmi"])
            print("Health:",data["data"]["health"])