"""Lesson 6B Sandbox
CS100: Roadmap to Computing
"""

# ---------- Quick Try 1: the third number ----------
# Run each one. Write down what you get.

for i in range(0, 10, 2):
    print(i)

# What changed? ______________________________


# Now make it count DOWN from 5 to 1.
# Hint: the third number can be negative.
for i in range(5, 0, -1):
    print(i)

# ---------- Quick Try 2: the accumulator ----------
# Add up 1 + 2 + 3 + 4 using a loop.
#
# You need a variable that survives BETWEEN runs of the loop.
# Think about where it has to be created.

total = 0          # <- outside

for i in range(1, 5):
    total += 2           # <- update it here

print(total)       # <- use it here. Should print 10.


# ---------- Quick Try 3: break it on purpose ----------
# Move the `total = 0` line INSIDE the loop (indent it).
# Run it again. What does it print now, and why?
