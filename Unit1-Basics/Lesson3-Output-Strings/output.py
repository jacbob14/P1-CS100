"""
Lesson 3: Output and Strings - STARTER FILE
CS100: Roadmap to Computing

INSTRUCTIONS
------------
Work through the parts in order. Each TODO tells you what to produce,
and "Expected:" shows exactly what should appear when you run the file.

Your job is to write code that matches the expected output exactly -
including spaces, capitalization, and punctuation.

Run the file often. Do not wait until the end.
    Right-click in this file -> "Run Python File in Terminal"

REMINDERS
---------
- No semicolons. Python does not use them.
- Save (Ctrl/Cmd + S) before you run, or you will run your old code.
- Commit and push your work when you finish each part.
"""


# =============================================================
# PART 1: print() vs console.log()
# =============================================================
print("----- PART 1 -----")

# TODO 1.1: Print the text: Hello, World!
# JavaScript was: console.log("Hello, World!");
# Expected: Hello, World!
print("Hello, World!")


# TODO 1.2: Print the three words Welcome, to, Python as separate
#           items in ONE print() call. Let the commas make the spaces.
# Expected: Welcome to Python
print("Welcome to Python")


# TODO 1.3: Print the label "Sum is" followed by the result of 7 + 3.
#           Do the math inside the print() call - do not type 10.
# Expected: Sum is 10
print("Sum is " + str(7 + 3))


# =============================================================
# PART 2: The sep and end parameters
# =============================================================
print("----- PART 2 -----")

# TODO 2.1: Print the three level names below joined by " > ".
#           Use the sep parameter. Do not build the string by hand.
# Expected: Level 1 > Level 2 > Level 3


# TODO 2.2: Print "a", "b", "c" with NOTHING between them.
# Expected: abc


# TODO 2.3: Use THREE separate print() calls to produce ONE line.
#           The end parameter controls what comes after each print.
# Expected: Ready...Set...GO!


# =============================================================
# PART 3: Repeating text with *
# =============================================================
print("----- PART 3 -----")

# TODO 3.1: Print a line of exactly 40 dash characters.
#           JavaScript was: "-".repeat(40)
# Expected: ----------------------------------------


# TODO 3.2: Print the text "Hi! " repeated 5 times.
#           Note the space inside the quotes - it stays in every copy,
#           so your output will end with a space you cannot see.
# Expected: Hi! Hi! Hi! Hi! Hi!


# TODO 3.3: Print a 3-line box around the word PYTHON.
#           The top and bottom borders must be the SAME WIDTH as
#           the middle line. Count the characters carefully.
# Expected:
# ==========
# = PYTHON =
# ==========


# =============================================================
# PART 4: Quotes inside strings
# =============================================================
print("----- PART 4 -----")

# TODO 4.1: Print this sentence, keeping the double quotes visible.
#           Hint: change the OUTER quotes.
# Expected: She said "nice play"


# TODO 4.2: Print this sentence, keeping the apostrophes visible.
# Expected: It's Bergen Tech's best team


# TODO 4.3: This one contains BOTH quote types, so switching the outer
#           quote is not enough on its own. Use escape characters,
#           or use triple quotes.
# Expected: He said "that's mine"


# =============================================================
# PART 5: f-strings
# =============================================================
print("----- PART 5 -----")

player = "Nova"
level = 12
score = 8400

# TODO 5.1: Use ONE f-string to print the sentence below.
#           Do not use + and do not use str().
# Expected: Nova reached level 12 with 8400 points!


# TODO 5.2: Print the player's score doubled. Do the multiplication
#           INSIDE the f-string braces - do not make a new variable.
# Expected: Double score: 16800


# TODO 5.3: Print the player's name in all capitals.
#           You can call a method inside the braces.
#           Hint: the string method is .upper()
# Expected: Welcome back, NOVA


# =============================================================
# PART 6: Escape sequences and triple quotes
# =============================================================
print("----- PART 6 -----")

item = "Headphones"
price = 24.99
qty = 2

# TODO 6.1: Use ONE print() with \n to produce two lines.
# Expected:
# Line 1
# Line 2


# TODO 6.2: Use \t to separate these three column headings.
# Expected: Name	Age	Grade


# TODO 6.3: Print this Windows file path. Remember that a backslash
#           has to be escaped to appear in output.
# Expected: File: C:\Users\Student


# TODO 6.4: Build a 3-line receipt using ONE triple-quoted f-string.
#           Calculate the total inside the braces.
#           Remember: triple quotes alone do NOT substitute variables.
#           You still need the f.
# Expected:
# Item: Headphones
# Quantity: 2
# Total: 49.98


# =============================================================
# CHALLENGE (optional)
# =============================================================
print("----- CHALLENGE -----")

# TODO: Convert this JavaScript block to Python.
#
#   let student = "Alex";
#   let subject = "Computer Science";
#   console.log("=".repeat(30));
#   console.log(`Student: ${student}`);
#   console.log(`Subject: ${subject}`);
#   console.log("=".repeat(30));
#
# Expected:
# ==============================
# Student: Alex
# Subject: Computer Science
# ==============================