"""Lesson 7B SANDBOX
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: don't trust the user ----------
# Ask for a number from 1 to 10. If it's outside that range, print
# "Try again" and ask again - as many times as it takes.
# Print "Thanks!" once you have a good one.
#
# Hint: you already know the priming read from 7A.


# ---------- Quick Try 2: roll until you get a six ----------
import random
random.seed(3)      # <- everyone in the room gets the SAME rolls

# Roll a die (1 to 6) until you get a 6.
# Print each roll, then how many rolls it took.
# Compare your count with the person next to you. It should match.
num = random.randint(1, 6)
while num != 6:
    
    num = random.randint(1, 6)