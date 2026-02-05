# temp=float(input("what is your current temp?"))
# if temp>30:
#     print("it's a hot day,Try swimming")
# else:
#     print("it's  a cool day")
# name = input("what is your name?")
# age=int(input("what is your age?"))
# if age >= 18:
#     print(name, " is eligible for voting")
# else:
#     print("not eligible for voting")
#
# marks=float(input("what is your marks?"))
# if marks >79 and marks<=100:
#     print(name,"you have an A grade")
# elif marks >60 and marks<=79:
#     print(name,"you have an B grade")
# elif marks >50 and marks<=60:
#     print(name,"you have an C grade")
# elif marks >30 and marks<=50:
#     print(name,"you have an D grade")
# elif marks >=0 and marks<30:
#     print(name,"you have an E grade")
# else:
#     print(name,"please enter a number between 0 and 100")

height = float(input("what is your height in meters? "))
weight = float(input("what is your weight in kg? "))
bmi = weight/(height**2)
print("your bmi is ",bmi)
if bmi<=18.5 :
    print("you are underweight")
elif bmi > 18.5 and bmi<=24.9:
    print("you are normal weight")
elif bmi > 25.0 and bmi<=29.9:
    print("you are overweight")
elif bmi >=30:
    print("you are obese")
