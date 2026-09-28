"""Lesson 4 Sandbox
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: four lines into one ----------
is_veteran = True
wins = 1
username = ""

# Rewrite each of these as a single ternary line.

# 1)
# if is_veteran:
#     badge = " *"
# else:
#     badge = ""

# your ternary here:
badge = " *" if is_veteran else ""


# 2)  careful - which way round does this go?
# if wins == 1:
#     word = "win"
# else:
#     word = "wins"

# your ternary here:
word = "win" if wins == 1 else "wins"

# 3)  a truthiness check inside a ternary
# if username:
#     greeting = username
# else:
#     greeting = "Guest"

# your ternary here:
greeting = username if username else "Guest"

# Print all three and check they still say the same thing.
print(f"Badge: {badge}")
print(f"Word: {word}")
print(f"Greeting: {greeting}")
print(" ")

# ---------- Quick Try 2: break it on purpose ----------
xp = 2500

# This works, but read it out loud first. How long does it take you
# to say what it does?

rank = "Gold" if xp >= 1500 else "Silver" if xp >= 500 else "Bronze"

print(rank)

# Now rewrite it as a normal if / elif / else chain.
# Which version would you rather find in someone else's code?
if xp >= 1500:
    rank = "Gold"
elif xp >= 500:
    rank = "Silver"
else:
    rank = "Bronze"

# ---------- Quick Try 3: chained comparison ----------
xp = 800

# Rewrite this using a chained comparison (the variable appears once):
# if xp >= 500 and xp < 1500:
#     print("Silver")
print("Silver") if xp >= 500 and xp < 1500 else ""
