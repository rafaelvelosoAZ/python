height = float(input("enter your height in cm: \n"))
weight = float(input("enter your weight in kg: \n"))

r = round(weight / (height/100) ** 2)

if r < 18.5:
    print("Your are underweight")
if r > 18.5 and r <= 25:
    print("Normal weight!")
elif r > 25 and r <= 30:
    print("Your are Overweight!")
elif r > 30 and r <= 35:
    print("Your are obese!")
else:
    print("Your are clinically obese!")