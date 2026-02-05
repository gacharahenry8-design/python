def hello_world():
    print("hello world")
hello_world()
def salute(name):
    print(f"Good morning {name}!")
salute('henry')
salute('sarah')
salute('Esther')
def greet(lastname,age):
    print(f'my name is {lastname} and I am {age} years old')
greet('Gathoni','20')
def sum(numb1,numb2):
    total = numb1 + numb2
    print(f'the sum is {total}')
sum(12,32)
sum(2134,45)
def multiply(num1,num2):
    return num1*num2
print(multiply(12,43))
print(multiply(71,89))

def check_number(number):
    if number > 0 :
        return 'the number is positive'
    elif number < 0 :
        return 'the number is negative'
    else:
        return 'the number is zero'
print(check_number(7))


def bmi(weight,height):
   return weight / (height ** 2)

print(bmi(64,1.345))
if bmi() <= 18.5:
    print("you are underweight")
elif bmi() > 18.5 and bmi() <= 24.9:
    print("you are normalweight")
elif bmi() > 25.0 and bmi() <= 29.9:
    print("you are overweight")
elif bmi() >= 30:
    print("you are obese")