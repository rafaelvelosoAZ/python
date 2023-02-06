y = int(input("type any year: \n"))

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print("It is a Leap Year!")
        else:
            print("It is not a Leap year!")
    else:
        print("It is a Leap Year!")
else:
    print("It is not a leap year!")