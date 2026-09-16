"""
Lesson 6 SANDBOX
CS100: Roadmap to Computing
"""


# =============================================================
# QUICK TRY 1 — comments and docstrings
# =============================================================

# TODO: add a header comment above this line with your name,
#       "Lesson 6 Sandbox", and today's date

# Jacob Bobrov | Lesson 6 Sandbox | 09/16/2026

# TODO: below, write a comment that explains WHY this line exists,
#       not what it does

WIDTH = 34 # Sets the maximum number of characters per line as 34


# =============================================================
# QUICK TRY 2 — shorter assignment
# =============================================================

total = 0
# total = total + 10
# total = total + 5
print(total)


# TODO: rewrite the two middle lines using += and check
#       you still get the same answer
total += 10
total += 5
print(total)

# =============================================================
# QUICK TRY 3 — find your way around
# =============================================================
# Do these in the TERMINAL, not in this file.
# Open it with Ctrl + `  (backtick, top-left under Escape)
#
# 1. pwd          where am I right now?
# 2. ls           what is in this folder?
# 3. cd ..        go up one level
# 4. pwd          confirm you moved
# 5. cd cs100     come back down (use Tab to autocomplete)
# 6. clear        tidy the screen
#
# Write what pwd printed the first time: /Users/jbobrov/Desktop/Coding/BT-COMPSCI/P1-CS100/Unit1-Basics/Lesson6-Comments-Style
#   ______________________________________________


# =============================================================
# QUICK TRY 4 — run this file from the terminal
# =============================================================

print("It ran from the terminal!")

# In the terminal:   python lesson7_sandbox.py
#
# Now deliberately break it:
#   1. cd ..  
#   2. python lesson7_sandbox.py    run it from the WRONG place
#   3. Read the error. Write the last line here: 
# /Library/Frameworks/Python.framework/Versions/3.13/Resources/Python.app/Contents/MacOS/Python: can't open file '/Users/jbobrov/Desktop/Coding/BT-COMPSCI/P1-CS100/Unit1-Basics/sandbox.py': [Errno 2] No such file or directory
#        ____________________________________________
#   4. cd back into the folder and run it again