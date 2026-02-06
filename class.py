class Cars:
    def __init__(self,make,model,price):
        self.brand = make
        self.model = model
        self.price = price
    def calculate_total(self, tax_rate):
        return self.price+(tax_rate * self.price)
Car1 = Cars("Toyota","supra",1300000)
Car2 = Cars("Toyota","Hilux",1550000)
Car3 = Cars("Ford","Ranger",1500000)
print(Car1.calculate_total(0.3))
print(Car2.calculate_total(0.3))
print(Car3.calculate_total(0.3))
