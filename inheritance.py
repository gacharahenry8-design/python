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

class Guest:
    def __init__(self,name,gender,room_type,bill_amount):
        self.name = name
        self.gender = gender
        self.room_type = room_type
        self.bill_amount = bill_amount

class VIP(Guest):
    def __init__(self,name,gender,room_type,bill_amount,vip_level):
        super().__init__(name,gender,room_type,bill_amount)
        self.VIP_level = vip_level
    def calculate_VIP_level(self, discount):
        return self.bill_amount+(self.VIP_level-(self.VIP_level*discount))
guest1 = Guest("Jimmie","Male","n.easternwing",12000)
guest2 = VIP("Sarah","Female","VIP_lounge",32500,47450)
print(guest2.calculate_VIP_level(0.2))