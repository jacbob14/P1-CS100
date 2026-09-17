"""
Lesson 7 Activity: Fix Four Bugs
CS100: Roadmap to Computing

This program has four bugs. Fix them ONE AT A TIME.
Run it from the terminal after every fix - each fix reveals the next.
"""

# BUG 1
team_name = "Red Hawks"
print("Team: " + team_name)

# BUG 2
games_played = 12
print("Games: " + str(games_played))

# BUG 3
ticket_price = int(float(("8.50")))
print(f"Ticket: ${ticket_price}")

# BUG 4
total_points = 87
print(f"Points per game: {int(total_points / games_played)}")
# This one does NOT crash. Run it and read the output.
# Something about the answer looks off. Can a team score
# a fraction of a point?


# =============================================================
# HOW TO WORK
# =============================================================
# In the terminal:   python lesson7_debug_starter.py
#
# For each bug:
#   1. Read the LAST line of the traceback - it names the problem
#   2. Read the "line N" - that is where to look
#   3. Fix it
#   4. Run again. The next bug appears.
#
# Write the error type for each bug here as you go:
#   Bug 1: NameError
#   Bug 2: TypeError
#   Bug 3: ValueError
#   Bug 4: Logic Error  (trick question - read it again)