"""Lesson 1 Sandbox
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1 ----------
health = 24
shields = 0
wins = 12

# print the answer: is health below 30?
print(health < 30)
# print the answer: are shields above 0?
print(shields > 0)
# print the answer: are wins exactly 12?
print(wins == 12)

# ---------- Quick Try 2: name your booleans ----------
level = 7
coins = 250
wins = 3

# is_low_level      -> level is under 10
is_low_level = level < 10
# can_afford_skin   -> the skin costs 300
can_afford_skin = coins >= 300
# ranked_ready      -> ranked needs 10 wins
ranked_ready = wins >= 10
# Now print all three with f-strings and look at the answers.
print(f"Is low level: {is_low_level}")
print(f"Can afford skin: {can_afford_skin}")
print(f"Ranked ready: {ranked_ready}")

# ---------- Type together: the when ----------
# Type this with the class, then run it.

health = 24
is_hurt = health < 30

# when is_hurt is true:
#     print "Low health!"
#     print "Find a medkit"
if is_hurt:
    print("Low Health!")
    print("Find a Medkit!")
else: 
    print("High Health!")
    print("Still standing!")
    
# print "Match continues"    <-- not indented
print("Match continues")

# ---------- Try it: what is inside the when ----------
# Change health to 90 and run it again.
# Which lines survived, and why?


# ---------- Quick Try 3, part 1: the other path ----------
# Add an else to the program above.
# Make it say "Still standing" when health is fine.


# ---------- Quick Try 3, part 2: decide, then use ----------
xp = 1450
title = ""

# if xp is 1000 or more, set title to "Veteran"
# otherwise set title to "Rookie"
if xp >= 1000:
    title = "Veteran"
else:
    title = "Rookie"
# print it ONCE, after the branches - not inside them
print(f"The title is: {title}")
# Then change xp to 200 and run it again.