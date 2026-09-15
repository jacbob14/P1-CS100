"""
Lesson 4 SANDBOX
CS100: Roadmap to Computing

Your sandbox for the two Quick Trys during class.

NOT SUBMITTED. Nothing here is graded. Break things, guess, delete,
try again. The graded work is lesson4_infocard_starter.py.
"""


# =============================================================
# QUICK TRY 1 — variables and types
# =============================================================
# These come pre-written. Run them and read the output.

player = "Nova"
level = 12
accuracy = 82.5
is_ranked = True

print(type(player))
print(type(level))
print(type(accuracy))
print(type(is_ranked))

# TODO: make a variable for your own favourite game and print its type
fav_game = "Minecraft"
print(type(fav_game))

# TODO: print the type of 42 and the type of 42.0
#       They look the same. They are not.
print(type(42))
print(type(42.0))

# =============================================================
# QUICK TRY 2 — conversion
# =============================================================
# Each line below is broken or surprising. Run them one at a time.

# TODO 1: this crashes. Run it, read the error, then fix it with str()
# print("Level " + level)
print("Level " + str(level))

# TODO 2: predict the output, then run it
# print(10 / 2)
print("5.0")
print(10/2)

# TODO 3: predict the output, then run it
# print(int(3.7))
print("3")
print(int(3.7))

# TODO 4: this crashes too. Why? What would work instead?
# print(int("3.7"))
print(int(float("3.7")))