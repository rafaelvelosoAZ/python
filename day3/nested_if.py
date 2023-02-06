#
# if condition
#   if another condition:
#       do this
#   else:
#       do this
# else:
#   do this
# 
print("Welcome to our rollercoaster!")
height = int(input("What is your height in cm ? \n"))
age = int(input("What is your age? \n"))

if height > 120:
    print("Can ride")
    if age < 12:
        print("Cost $5 dolars!")
    elif age <= 18:
        print("Cost $7 dolars!")
    elif age == 15:
        print("Cost $1000 dolars")
    elif age >= 88:
        print("Its free")
    else:
        print("Cost $12 dolars!")
else:
    print("Cant ride!")