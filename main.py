print("Welcome to the Love Calculator!\n.")
# input the names which will be converted to lower cases.
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

# Concat the names to make a single string.
name = name1 + " " + name2
# Check the presence of the letters in the names given.
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
# Add the count of the letters and change it to string.
true = str(t + r + u + e)
# Check the presence of the letters in the names given.
l = name.count("l")
o = name.count("o")
v = name.count("v")
# Add the count of the letters and change it to string.
love = str(l + o + v + e)

# concat the two strings and convert them to strings.
true_love = int(true + love)
# Do the comparison on the score.
if true_love < 10 or true_love >90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 and true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}, maybe try seeing other people.")

