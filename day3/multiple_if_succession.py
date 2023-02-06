height = int(input("What is your height in cm ?: \n"))
if height >= 120:
    age = int(input("what is your age?: \n"))
    if age < 12:
        bill = 5
        photo = input("Whant a photo? \n")
        if photo == "Y":
            bill += 3
            print(f"The total bill is {bill}")
        else:
            print(f"The total is {bill}")
    elif age < 18:
        bill = 7
        photo = input("Whant a photo? \n")
        if photo == "Y":
            bill += 3
            print(f"The total bill is {bill}")
        else:
            print(f"The total is {bill}")
    elif age >= 18:
        bill = 12
        photo = input("Whant a photo? \n")
        if photo == "Y":
            bill += 3
            print(f"The total is {bill}")
        else:
            print(f"The total is {bill}")
else:
    print("cant ride!")
    