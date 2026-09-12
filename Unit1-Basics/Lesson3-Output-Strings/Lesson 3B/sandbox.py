"""
Lesson 3B SANDBOX
CS100: Roadmap to Computing

Your sandbox for the Quick Try during class.

NOT SUBMITTED. Nothing here is graded. The graded work is
lesson3B_recap_starter.py.

Run it as often as you like:
    Right-click in this file -> "Run Python File in Terminal"
"""


# =============================================================
# QUICK TRY — f-strings
# =============================================================

player = 'Nova'
level = 12
score = 8400

# TODO 1: Use ONE f-string to print exactly:
#         Nova reached level 12 with 8400 points!
print(f"{player} reacher level {level} with {score} points!")

# TODO 2: Print the score doubled. Do the math INSIDE the braces -
#         do not make a new variable.
#         Double score: 16800
print(f"Double score: {score * 2}")

# =============================================================
# SPACE TO EXPERIMENT
# =============================================================
# Use the room below to try anything from the lesson: escape
# sequences, triple quotes, or an f-string you are unsure about.
#
# Two worth testing yourself, because seeing them fail is how
# they stick:
#
#   print("Hi {player}")        <- what happens without the f?
#   print("""Hi {player}""")    <- do triple quotes substitute?