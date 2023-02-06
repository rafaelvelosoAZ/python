print("Welcome to pizaa deliveries!")
size = input("What size do you want? S, M or L ? \n")
add_pepperoni = input("Do you want pepperoni ? \n")
extra_cheese = input("Do you want extra cheese ? \n")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill +=2
        if extra_cheese == "Y":
            bill +=1
            print(f"the total bill is ${bill}")
        else:
            print(f"the total bill is ${bill}")
    else:
        print(f"the total bill is ${bill}")

elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill +=3
        if extra_cheese == "Y":
            bill +=1
            print(f"the total bill is ${bill}")
        else:
                print(f"the total bill is ${bill}")
    else:
        print(f"the total bill is ${bill}")

elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill +=3
        if extra_cheese == "Y":
            bill +=1
            print(f"the total bill is ${bill}")
        else:
                print(f"the total bill is ${bill}")
    else:
        print(f"the total bill is ${bill}")
else:
    print("Please select one of our option S, M or L!")
