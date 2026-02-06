class Patient:
    def __init__(self,name,gender,diagnosis,amount_to_pay):
        self.name = name
        self.gender = gender
        self.diagnosis = diagnosis
        self.amount_to_pay = amount_to_pay
class Inpatient(Patient):
    def __init__(self,name,gender,diagnosis,amount_to_pay,days_admitted):
        super().__init__(name, gender, diagnosis, amount_to_pay)
        self.days_admitted = days_admitted
patient1 = Patient("James","Male","Malaria",15000)
patient2 = Inpatient("Maggie","Female","labour",27500,3)
