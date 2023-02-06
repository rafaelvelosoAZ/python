print("Welcome to rollercoaster!")
height = int(input("What is your height? \n"))
age = int(input("What is your age? \n"))

if height >= 120:
    if age < 12:
        bill = 5
        if input("Want photos? \n") == "Y":
            bill += 3
            print(f"The total cost is: ${bill}")
        else:
            print(f"The total cost is: ${bill}")
    elif age >= 12 and age < 18:
        bill = 7
        if input("Want photos? \n") == "Y":
            bill += 3
            print(f"The total cost is: ${bill}")
        else:
            print(f"The total cost is: ${bill}")
    elif age >= 18 and age < 45:
        bill = 12
        if input("Want photos? \n") == "Y":
            bill += 3
            print(f"The total cost is: ${bill}")
        else:
            print(f"The total cost is: ${bill}")
    elif age >= 45 and age < 55:
        bill = 0
        if input("Want photos? \n") == "Y":
            bill += 3
            print(f"The total cost is: ${bill}")
        else:
            print(f"The total cost is: ${bill}")
    elif age >= 55:
       print("All the things will be free, also you could include a photo!")
else:
    print("cant ride!")