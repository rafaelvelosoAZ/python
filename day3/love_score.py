print("Welcome to love calculator")

name1 = input("name1 here: \n")
name2 = input("name2 here: \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

t = int(name2_lower.count("t") + name1_lower.count("t"))
r = int(name2_lower.count("r") + name1_lower.count("r"))
u = int(name2_lower.count("u") + name1_lower.count("u"))
e = int(name2_lower.count("e") + name1_lower.count("e"))

l = int(name2_lower.count("l") + name1_lower.count("l"))
o = int(name2_lower.count("o") + name1_lower.count("o"))
v = int(name2_lower.count("v") + name1_lower.count("v"))
e = int(name2_lower.count("e") + name1_lower.count("e"))

r1 = t + r + u + e
r2 = l + o + v + e

r3_str = str(r1)+str(r2)
r4_int = int(r3_str)

if r4_int < 10 or r4_int > 90:
    print(f"Your score is {r3_str}, you go together like coke and mentos.")
elif r4_int >= 40 and r4_int <= 50:
    print(f"Your score is {r3_str}, you are alright together.")
else:
    print(f"Your score is {r3_str}.")