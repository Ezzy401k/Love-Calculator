print("Welcome to the Love Calculator!\n.")
name1 = input("What is your name? ").lower()
name2 = input("Whar is their name? ").lower()

name = name1 + " " + name2
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
true = str(t + r + u + e)

l = name.count("l")
o = name.count("o")
v = name.count("v")
love = str(l + o + v + e)

true_love = int(true + love)
if true_love < 10 or true_love >90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}, maybe try seeing other people.")

