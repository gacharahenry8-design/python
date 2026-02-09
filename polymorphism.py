class Kenyan:
    def speak(self):
        print("I can speak")
class Maasai(Kenyan):
    def speak(self):
        print("I can speak maasai")
class Turkana(Kenyan):
    def speak(self):
        print("I can speak turkana")
Kenyan1 = Kenyan()
Kenyan1.speak()
maasai1 = Maasai()
maasai1.speak()
turkana1 = Turkana()
turkana1.speak()
print(turkana1.speak)
