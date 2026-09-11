"""
Lesson 3A SANDBOX
CS100: Roadmap to Computing

Your sandbox for the four Quick Trys during class.

NOT SUBMITTED. Nothing here is graded. Break things, guess, delete,
try it again. The graded work is lesson3A_banner_starter.py.

Run it as often as you like:
    Right-click in this file -> "Run Python File in Terminal"
"""


# =============================================================
# QUICK TRY 1 — print()
# =============================================================
# Run each of these. Notice where the spaces come from.

print('Welcome to Python!')
print("Double quotes work too")
print('Welcome', 'to', 'Python!')
print('Sum is', 7 + 3)


# =============================================================
# QUICK TRY 2 — sep and end
# =============================================================
# PREDICT each output before you run it.

# Should print:  Level 1 > Level 2 > Level 3
print('Level 1', 'Level 2', 'Level 3', sep=' > ')

# These three should land on ONE line
print('Ready', end='')
print('...Set', end='')
print('...GO!')


# =============================================================
# QUICK TRY 3 — repeating with *
# =============================================================
# Predict how wide each line will be BEFORE you run it.

# TODO: print a line of 40 dashes
print("-" * 40)

# TODO: print "Hi! " repeated 5 times
print("Hi!" * 5)

# TODO: print a 3-line box around the word PYTHON
#       The borders must match the middle line's width.
print("========")
print("|Python|")
print("========")

# =============================================================
# QUICK TRY 4 — quotes
# =============================================================
# Print each of these exactly.

# TODO 1:  She said "nice play"
print('She said "nice play"')

# TODO 2:  It's Bergen Tech's best team
print("It's Bergen Tech's best team")

# TODO 3:  He said "that's mine"
#          This one has BOTH quote types - switching the outer
#          quote alone will not save you.
print("He said ", end = '')
print('"that', end = '')
print("'s mine", end = '')
print('"')