"""Unit 3 Lesson 1D - Round 2: Fix the Factory
CS100: Roadmap to Computing

Six machines are broken. Each one has exactly ONE bug.

Run the file. Every FAIL line tells you what the machine gave back and what
it SHOULD have given back. Fix a machine, run again, and watch its FAIL turn
into PASS. Then write one sentence under it: what was wrong?

Stars: 1 for every machine you fix. Six machines, six stars.
Don't change anything inside the TEST HARNESS box.
"""

# ======================== TEST HARNESS - don't change ========================
fixed = 0

def check(name, got, want):
    """Print PASS or FAIL for one machine."""
    global fixed
    if got == want:
        fixed = fixed + 1
        print("PASS", name)
    else:
        print("FAIL", name, "- got", repr(got), "but expected", repr(want))
# =============================================================================


# ---------- Machine 1: the doubler ----------
def double(n):
    """Return n times 2."""
    return n * 2

result1 = double(21)          # Machine 1 should hold the double of 21
check("Machine 1", result1, 42)
# What was wrong: Machine 1 was already working correctly as an example.


# ---------- Machine 2: the label maker ----------
def make_label(name, role):
    """Return text like "Ana the Engineer"."""
    return name + " the " + role

result2 = make_label("Ana", "Engineer")
check("Machine 2", result2, "Ana the Engineer")
# What was wrong: The arguments were passed in reverse order (role before name).


# ---------- Machine 3: the area meter ----------
def area(width, height):
    """Return the area of a rectangle."""
    return width * height

result3 = area(3, 4)
check("Machine 3", result3, 12)
# What was wrong: The function used print() instead of return, returning None.


# ---------- Machine 4: the grader ----------
def grade(score):
    """Return a letter grade: A for 90+, B for 80+, C for 70+, F for anything lower."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

check("Machine 4", grade(55), "F")
# What was wrong: Missing an else clause to return "F" for scores lower than 70.


# ---------- Machine 5: the vowel counter ----------
def count_vowels(word):
    """Return how many vowels are in the word."""
    count = 0
    for ch in word:
        if ch in "aeiou":
            count = count + 1
    return count

check("Machine 5", count_vowels("banana"), 3)
# What was wrong: return count was indented inside the for loop, exiting on the first letter.


# ---------- Machine 6: the bonus machine ----------
def add_bonus(score):
    """Return the score plus a 10 point bonus."""
    bonus = 10
    return score + bonus

points = 50
points = add_bonus(points)
check("Machine 6", points, 60)
# What was wrong: The function did not return the new score, and the caller did not assign the returned value back to points.


print()
print("Machines fixed:", fixed, "of 6   stars:", fixed)
